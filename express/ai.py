from google.cloud import documentai_v1beta3 as documentai
import json
import re
def parse_pdf_to_json(project_id: str, location: str, processor_id: str, file_path: str):
    client = documentai.DocumentProcessorServiceClient()

    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    with open(file_path, "rb") as image:
        image_content = image.read()

    document = {"content": image_content, "mime_type": "application/pdf"}

    request = {"name": name, "document": document}
    result = client.process_document(request=request)

    text = result.document.text
    # Extract additional specific information from the text using regular expressions
    carrier_name = re.search(r"CARRIER NAME:\s*(.*)", text)
    carrier_name = carrier_name.group(1) if carrier_name else None

    backup_contact_name = re.search(r"FE Backup Contact Name\s*\n(.*)", text)
    backup_contact_name = backup_contact_name.group(1) if backup_contact_name else None

    sap_number = re.search(r"SAP #\s*\n(\d+)", text)
    sap_number = sap_number.group(1) if sap_number else None

    fe_contact_name = re.search(r"FE Contact Name\s*\n(.*)", text)
    fe_contact_name = fe_contact_name.group(1) if fe_contact_name else None

    dropoff_date = re.search(r"dropoff\s*\n(.*\s*PM)", text)
    dropoff_date = dropoff_date.group(1) if dropoff_date else None

    flat_rate = re.search(r"Flat Rate\s*\n(\d+)", text)
    flat_rate = flat_rate.group(1) if flat_rate else None

    subtotal = re.search(r"Subtotal\s*\n(\d+.\d+)", text)
    subtotal = subtotal.group(1) if subtotal else None

    # Update the JSON object with the additional extracted information
    # json_data.update({
    #     "carrier_name": carrier_name,
    #     "backup_contact_name": backup_contact_name,
    #     "sap_number": sap_number,
    #     "fe_contact_name": fe_contact_name,
    #     "dropoff_date": dropoff_date,
    #     "flat_rate": flat_rate,
    #     "subtotal": subtotal
    # })
    # Extract specific information from the text using regular expressions
    load_id = re.search(r"LOAD #:\s*(\w+-\d+)", text)
    load_id = load_id.group(1) if load_id else None

    date = re.search(r"DATE:\s*(.*),\s*(\d+:\d+\s*[a|p].m.)", text)
    date = date.group(1) + ', ' + date.group(2) if date else None

    weight = re.search(r"WEIGHT:\s*(\d+)", text)
    weight = weight.group(1) if weight else None

    mc_number = re.search(r"MC NUMBER:\s*(\d+)", text)
    mc_number = mc_number.group(1) if mc_number else None

    email = re.search(r"FE Backup Contact Email\s*\n(\S+@\S+)", text)
    email = email.group(1) if email else None

    po_number = re.search(r"PO Number\s*\n(\d+)", text)
    po_number = po_number.group(1) if po_number else None

    contact_number = re.search(r"FE Contact Number\s*\n(\d+)", text)
    contact_number = contact_number.group(1) if contact_number else None

    pickup_date = re.search(r"pickup\s*\n(.*\s*PM)", text)
    pickup_date = pickup_date.group(1) if pickup_date else None

    # Construct a JSON object from the extracted information
    json_data = {
        "carrier_name": carrier_name,
        "backup_contact_name": backup_contact_name,
        "sap_number": sap_number,
        "fe_contact_name": fe_contact_name,
        "dropoff_date": dropoff_date,
        "flat_rate": flat_rate,
        "subtotal": subtotal,
        "load_id": load_id,
        "date": date,
        "weight": weight,
        "mc_number": mc_number,
        "email": email,
        "phone_number": po_number,
        "contact_number": contact_number,
        "pickup_date": pickup_date
    }

    return json_data

# print(json.dumps(parse_pdf_to_json("genial-venture-420603", "us", "8f10563b5134e1e8", "Rc # INT-13745.pdf"), indent=4))