import dataclasses


@dataclasses.dataclass
class Service:
    name: str
    short_description: str
    long_description: str
    display: bool
    icon: str

@dataclasses.dataclass
class ServiceDetail:
    service: Service
    name: str
    description: str

services = [
    Service(
        name="Accountancy Services",
        short_description="We provide bespoke accountancy services to our clients ranging from start-ups to Public Interest Entities."
    ),
    Service(
        name="Corporate Finance",
        short_description="At Abhasa Financial Services, we work closely with our clients to determine any funding requirement for their business growth and/or acquisition of new businesses."
    ),
    Service(
        name="Tax Services",
        short_description="at abhasa financial services, we work closelywith our clients to determine any funding requirement for their business growth and / or acquisition of new businesses."
    ),
    Service(
        name="Permit & Licence Applications",
        short_description="To start a business in Mauritius, companies need to be aware of the different permits and licenses to apply for pertaining to their business activities.",
    ),
    Service(
        name="Information Technology",
        short_description="Our team advises you on the appropriate accountancy software for SME to implement and for more complex businesses we can assist in selecting your ERP solution provider.",
    ),
    Service(
        name="Payroll Solutions",
        short_description="Our payroll services include the monthly preparation of payslips, filing of monthly and annual returns; and the preparation of yearly Statement of Emoluments."
    ),
    Service(
        name="Corporate Secretarial Finance",
        short_description="Abhasa Limited provides a full fledge secretarial services to our clients to ensure compliance with the provisions of the Companies Act 2001."
    ),
    Service(
        name="Advisory Services for Start-Up",
        short_description="We appreciate the difficulties and challenges facing most start-ups and we devote considerable time to our clients in order to ensure that they have the necessary information and advice before registering a new business."
    ),

]