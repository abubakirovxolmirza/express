from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Load, Stops
from django.dispatch import receiver
from django.db.models.signals import post_save
import json
from .ai import parse_pdf_to_json

@receiver(post_save, sender=Load)
def send_email(sender, instance, created, **kwargs):
    if not instance.ai:
        return
    if created:
        # Parse the PDF to JSON
        json_data = parse_pdf_to_json("genial-venture-420603", "us", "8f10563b5134e1e8", instance.rate_con.path)

        # Update the load_id field with the Bill of Lading Number
        instance.load_id = json_data["load_id"]
        instance.company_name = json_data["carrier_name"]
        instance.created_date = json_data["pickup_date"]
        
        instance.email = json_data["email"]
        instance.save()
        if 'pickup_date' in json_data:
            Stops.objects.create(load=instance, stop_name='Pickup', address1=json_data['pickup_date'])
        if 'dropoff_date' in json_data:
            Stops.objects.create(load=instance, stop_name='Delivery', address1=json_data['dropoff_date'])