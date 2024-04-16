from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Driver(models.Model):
    DRIVER_LICENSE_STATE = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),

    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('ACTIVE (DF)', 'ACTIVE (DF)'),
        ('Terminate', 'Terminate'),
        ('Applicant', 'Applicant'),

    ]

    DRIVER_STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Home', 'Home'),
        ('In-Transit', 'In-Transit'),
        ('Inactive', 'Inactive'),
        ('Shop', 'Shop'),
        ('Rest', 'Rest'),
        ('Dispatched', 'Dispatched'),

    ]

    DL_CLASS_STATUS_CHOICES = [
        ('Unknown', 'Unknown'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('Other', 'Other'),
    ]

    DRIVER_TYPE_CHOICES = [
        ('COMPANY_DRIVER', 'Company_driver'),
        ('OWNER_OPERATOR', 'Owner_operator'),
        ('LEASE', 'Lease'),
        ('RENTAL', 'Rental'),
    ]

    TEAM_DRIVER_CHOICES = [
        ('DRIVER_2', 'Driver_2'),
        ('ASSIGNED_DISPATCHER', 'Assigned_dispatcher'),
        ('PERCENT_SALARY', 'Percent_salary'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    birth_date = models.DateField(blank=True, null=True)

    employment_status = models.CharField(max_length=50, choices=EMPLOYMENT_STATUS_CHOICES)
    telegram_username = models.CharField(max_length=100, blank=True, null=True)
    driver_status = models.CharField(max_length=50, choices=DRIVER_STATUS_CHOICES)
    company_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    password = models.CharField(max_length=100)

    driver_license_id = models.CharField(max_length=50)
    dl_class = models.CharField(max_length=10, choices=DL_CLASS_STATUS_CHOICES, blank=True, null=True)
    driver_type = models.CharField(max_length=50)
    driver_license_state = models.CharField(max_length=50, choices=DRIVER_LICENSE_STATE)
    driver_license_expiration = models.DateField(blank=True, null=True)

    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)

    assigned_truck = models.ForeignKey('Truck', related_name='TRUCK_DRIVERS', on_delete=models.CASCADE)
    assigned_trailer = models.ForeignKey('Trailer',  related_name='TRailer_DRIVERS', on_delete=models.CASCADE)
    assigned_dispatcher = models.ForeignKey('Dispatcher', related_name='dispatcher_drivers', on_delete=models.CASCADE)
    other_id = models.CharField(max_length=100, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)
    tariff = models.IntegerField(blank=True, null=True)
    mc_number = models.CharField(max_length=50, blank=True, null=True)
    driver_tags = models.ForeignKey('DriverTags', related_name='drivertags', on_delete=models.CASCADE)
    team_driver = models.CharField(max_length=50, choices=TEAM_DRIVER_CHOICES)
    permile = models.FloatField()
    cost = models.FloatField()
    payd = models.FloatField()

    def __str__(self):
        return self.first_name


class Trailer(models.Model):
    TYPE_CHOICES = (
        ('REEFER', 'Reefer'),
        ('DRYVAN', 'Dryvan'),
        ('STEPDECK', 'Stepdeck'),
        ('LOWBOY', 'Lowboy'),
        ('CARHAUL', 'Carhaul'),
        ('FLATBED', 'Flatbed'),
    )

    OWNER_CHOICES = (
        ('RYDER', 'Ryder'),
        ('PENSKE', 'Penske'),
        ('ADD VENDOR', 'Add Vendor'),
    )

    OWNERSHIP_CHOICES = (
        ('COMPANY', 'Company'),
        ('OWNER_OPERATOR', 'Owner-operator'),
        ('LEASE', 'Lease'),
        ('RENTAL', 'Rental'),
    )

    INTEGRATION_ELD_CHOICES = (
        ('ELD', 'Eld'),
        ('MOBILE', 'Mobile'),
        ('TELEMATICS', 'Telematics'),
        ('OTHER', 'Other'),
    )

    make = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    ownership = models.CharField(max_length=20, choices=OWNERSHIP_CHOICES)

    vin = models.CharField(max_length=20, blank=True)
    owner = models.CharField(max_length=50, choices=OWNER_CHOICES, blank=True, null=True)
    mc_number = models.CharField(max_length=20)
    year = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=50)
    unit_number = models.IntegerField()
    plate_number = models.CharField(max_length=20, blank=True, null=True)
    last_annual_inspection_date = models.DateField(blank=True, null=True)
    registration_expiry_date = models.DateField(blank=True, null=True)
    notes = models.TextField()

    integration_eld = models.CharField(max_length=50, choices=INTEGRATION_ELD_CHOICES, blank=True, null=True)
    integration_id = models.CharField(max_length=50, blank=True, null=True)
    integration_api = models.CharField(max_length=50, blank=True, null=True)
    tags = models.ForeignKey('TrailerTags', related_name='trailertags', on_delete=models.CASCADE)
    driver = models.CharField(max_length=50)
    co_driver = models.CharField(max_length=50, blank=True, null=True)
    drop_date = models.DateField(blank=True, null=True)
    pickup_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.unit_number}"


class TrailerTags(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class DriverTags(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Truck(models.Model):
    ASSIGNMENT_STATUS_CHOICES = (
        ('AVAILABLE', 'Company'),
        ('INACTIVE', 'Inactive'),

    )
    OWNERSHIP_CHOICES = (
        ('COMPANY', 'Company'),
        ('OWNER_OPERATOR', 'Owner-operator'),
        ('LEASE', 'Lease'),
        ('RENTAL', 'Rental'),
        ('OTHER', 'Other'),
    )

    OWNER_CHOICES = (
        ('COMPANY', 'Company'),
        ('OWNER_OPERATOR', 'Owner-operator'),
        ('LEASE', 'Lease'),
        ('RENTAL', 'Rental'),
        ('OTHER', 'Other'),
    )
    INTEGRATION_ELD_CHOICES = (
        ('ELD', 'Eld'),
        ('MOBILE', 'Mobile'),
        ('TELEMATICS', 'Telematics'),
        ('OTHER', 'Other'),
    )

    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),

    ]
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    unit_number = models.IntegerField()
    plate_number = models.CharField(max_length=50)
    vin = models.CharField(max_length=20)
    year = models.IntegerField()
    state = models.CharField(max_length=20, choices=STATE_CHOICES)

    weight = models.IntegerField(blank=True, null=True)

    registration_expiry_date = models.DateField(blank=True, null=True)
    last_annual_inspection_date = models.DateField(blank=True, null=True)

    color = models.CharField(max_length=50, blank=True, null=True)
    integration_eld = models.CharField(max_length=50, choices=INTEGRATION_ELD_CHOICES, blank=True, null=True)
    integration_id = models.IntegerField(blank=True, null=True)
    integration_api = models.CharField(max_length=50, blank=True, null=True)

    ownership_type = models.CharField(max_length=20, choices=OWNERSHIP_CHOICES)
    tags = models.ForeignKey('TruckTags', related_name='trucktags', on_delete=models.CASCADE)
    mc_number = models.CharField(max_length=50)
    pickup_odometer = models.CharField(max_length=50, blank=True, null=True)
    owner = models.CharField(max_length=50, choices=OWNER_CHOICES, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    assignment_status = models.CharField(max_length=50, choices=ASSIGNMENT_STATUS_CHOICES)
    driver = models.CharField(max_length=50)
    co_driver = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    pickup_date = models.DateField(blank=True, null=True)
    drop_date = models.DateField(blank=True, null=True)
    mileage_on_pickup = models.IntegerField(blank=True, null=True)
    mileage_on_drop = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.unit_number}"


class TruckTags(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.tag


class Dispatcher(models.Model):
    EMPLOYMENT_STATUS_CHOICES = [
        ('ACTIVE (DF)', 'ACTIVE (DF)'),
        ('Terminate', 'Terminate'),
        ('Applicant', 'Applicant'),
    ]

    MC_NUMBER_CHOICES = [
        ('ADMIN OR COMPANY MC', 'Admin or Company MC'),
    ]

    POSITION_CHOICES = [
        ('EMPLOYEE', 'Employee'),
        ('MANAGER', 'Manager'),
    ]

    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    employee_status = models.CharField(max_length=50, choices=EMPLOYMENT_STATUS_CHOICES)
    mc_number = models.CharField(max_length=50, choices=MC_NUMBER_CHOICES)
    contact_number = models.CharField(max_length=50)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    company_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    password = models.CharField(max_length=50)
    office = models.CharField(max_length=50, blank=True, null=True)
    dispatcher_tags = models.ForeignKey('DispatcherTags', related_name='dispatchertags', on_delete=models.CASCADE)

    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, default='USA', blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nickname


class DispatcherTags(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.tag


class Employee(models.Model):

    EMPLOYMENT_STATUS_CHOICES = [
        ('ACTIVE (DF)', 'ACTIVE (DF)'),
        ('Terminate', 'Terminate'),
        ('Applicant', 'Applicant'),
    ]

    POSITION_CHOICES = [
        ('ACCOUNTING', 'Accounting'),
        ('FLEET MANAGMENT', 'Fleet Managment'),
        ('SAFETY', 'Safety'),
        ('HR', 'hr'),
        ('UPDATER', 'Updater'),
        ('ELD TEAM', 'ELD team'),
        ('OTHER', 'Other'),
    ]

    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    ]
    company_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    employee_tags = models.ForeignKey('EmployeeTags', related_name='employeetags', on_delete=models.CASCADE)
    email_address = models.EmailField()
    password = models.CharField(max_length=50)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    contact_number = models.CharField(max_length=50)
    employee_status = models.CharField(max_length=50, choices=EMPLOYMENT_STATUS_CHOICES)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default='USA')
    zip_code = models.IntegerField()
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    city = models.CharField(max_length=50)
    note = models.CharField(max_length=50, blank=True, null=True)


class EmployeeTags(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.tag


class CustomerBroker(models.Model):
    BILLING_TYPE_CHOICES = [
        ('NONE', 'None'),
        ('FACTORING_COMPANY', 'Factoring_company'),
        ('EMAIL', 'Email'),
        ('MANUAL', 'Manual'),
    ]

    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    ]
    company_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    mc_number = models.CharField(max_length=50)
    pod_file = models.BooleanField(default=False)
    rate_con = models.BooleanField(default=False)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default='USA')
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=50)
    billing_type = models.CharField(max_length=50, choices=BILLING_TYPE_CHOICES)
    terms_days = models.DateTimeField()

    def __str__(self):
        return self.company_name


class LoadTags(models.Model):
    TAG_CHOICES = [
        ('HAZ', 'Haz'),
        ('DEDICATED LANE', 'Dedicated Lane'),
        ('HOT LOAD', 'Hot Load'),
        ('ISSUE', 'Issue'),
    ]

    tag = models.CharField(max_length=50, choices=TAG_CHOICES)

    def __str__(self):
        return self.tag


class Load(models.Model):
    TAGS_CHOICES = [
        ('HAZ', 'Haz'),
        ('DEDICATED-LINE', 'Dedicated-Line'),

    ]

    EQUIPMENT_TYPE_CHOICES = [
        ('DRYVAN', 'Dryvan'),
        ('REEFER', 'Reefer'),
        ('CARHAUL', 'Carhaul'),
        ('FLATBED', 'Flatbed'),
        ('STEPDECK', 'Stepdeck'),
        ('POWERONLY', 'PowerOnly'),
        ('RGN', 'Rgn'),
        ('TANKERSTYLE', 'TankerStyle'),
    ]

    LOAD_STATUS_CHOICES = [
        ('OFFER', 'Offer'),
        ('BOOKED', 'Booked'),
        ('DISPATCHED', 'Dispatched'),
        ('INTRANSIT', 'Intransit'),
        ('DELIVERED', 'Delivered'),
        ('INVOICED', 'Invoiced'),
        ('PAID', 'Paid'),
    ]
    created_by = models.ForeignKey('Dispatcher', related_name='dispatcher', on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    load_id = models.IntegerField(blank=True, null=True)
    trip_id = models.IntegerField(blank=True, null=True)
    customer_broker = models.ForeignKey('CustomerBroker', related_name='customer_broker', on_delete=models.CASCADE, blank=True, null=True)
    driver = models.ForeignKey('Driver', related_name='driver', on_delete=models.CASCADE, blank=True, null=True)
    co_driver = models.CharField(max_length=100, null=True, blank=True)
    truck = models.ForeignKey('Truck', related_name='truck', on_delete=models.CASCADE, blank=True, null=True)
    dispatcher = models.ForeignKey('Dispatcher', related_name='created_by', on_delete=models.CASCADE, blank=True, null=True)
    load_status = models.CharField(max_length=50, choices=LOAD_STATUS_CHOICES, blank=True, null=True)
    tags = models.ForeignKey('LoadTags', related_name='loadtags', on_delete=models.CASCADE, blank=True, null=True)
    equipment_type = models.CharField(max_length=50, choices=EQUIPMENT_TYPE_CHOICES, blank=True, null=True)
    trip_status = models.CharField(max_length=50, blank=True, null=True)
    invoice_status = models.CharField(max_length=50, blank=True, null=True)
    trip_bil_status = models.CharField(max_length=50, blank=True, null=True)
    load_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    driver_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    per_mile = models.IntegerField(blank=True, null=True)
    mile = models.IntegerField(blank=True, null=True)
    empty_mile = models.IntegerField(blank=True, null=True)
    total_miles = models.IntegerField(blank=True, null=True)
    flagged = models.BooleanField(default=False, blank=True, null=True)
    flagged_reason = models.CharField(max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    chat = models.TextField(blank=True, null=True)
    rate_con = models.FileField(blank=True, null=True)
    bol = models.FileField(blank=True, null=True)
    pod = models.FileField(blank=True, null=True)
    document = models.FileField(blank=True, null=True)
    comercial_invoice = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"DT-{self.id}"


class Stops(models.Model):
    STOP_NAME_CHOICES = [
        ('PICKUP', 'Pickup'),
        ('DELIVERY', 'Delivery')
    ]

    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    ]
    load = models.ForeignKey(Load, on_delete=models.CASCADE, related_name='stops')
    stop_name = models.CharField(max_length=50, choices=STOP_NAME_CHOICES)
    company_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    reference_id = models.IntegerField()
    appointmentdate = models.DateField()
    time = models.TimeField()
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default='USA')
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    note = models.CharField(max_length=100)


class OtherPay(models.Model):
    PAY_CHOICES = [
        ('ACCESSORIALS', 'Accessorials'),
        ('PAYAMOUNT', 'PayAmount'),
        ('OTHERCHARGES', 'OtherCharges'),
        ('FUEL', 'Fuel'),
        ('BROKERFEE', 'BrokerFee'),
    ]

    TYPE_CHOICES = [
        ('DETENTION', 'Detention'),
        ('EMPTYMILES', 'EmptyMiles'),
        ('EXTRAMILES', 'ExtraMiles'),
        ('FLAT', 'Flat'),
        ('LAYOVER', 'Layover'),
        ('LINEHOUL', 'Linehoul'),
        ('FUELSURCHARGE', 'FuelSurcharge'),
        ('LUMPER', 'Lumper'),
        ('EXTRASTOP', 'ExtraStop'),
        ('TONU', 'TONU'),
        ('BONUS', 'Bonus'),
        ('OTHER', 'Other'),
    ]
    load = models.ForeignKey(Load, on_delete=models.CASCADE, related_name='otherpay')
    pay = models.CharField(max_length=50, choices=PAY_CHOICES)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200, blank=True, null=True)


class Commodities(models.Model):
    DESCRIPTION_CHOICES = [
        ('GENERALFREIGHT', 'GeneralFreight'),
        ('AUTOPARTS', 'AutoParts'),
        ('CHIP', 'Chip'),
        ('WATER', 'Water'),
        ('VEHICLE', 'Vehicle'),
        ('OTHER', 'Other'),
    ]
    load = models.ForeignKey(Load, on_delete=models.CASCADE, related_name='commodities')
    descriptions = models.CharField(max_length=100, choices=DESCRIPTION_CHOICES)
    qty = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    pcs = models.CharField(max_length=50)
    totalwt = models.CharField(max_length=50)
    width = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField()
    note = models.CharField(max_length=200, blank=True, null=True)
