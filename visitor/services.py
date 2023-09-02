import dataclasses


@dataclasses.dataclass
class ServiceDetail:
    description: str

@dataclasses.dataclass
class Service:
    name: str
    short_description: str
    icon: str
    path: str
    long_description: str
    details: list[str] | None = None

services = [
    Service(
        path="accountancy-services",
        name="Accountancy Services",
        icon="calculator",
        short_description="We provide bespoke accountancy services to our clients ranging from start-ups to Public Interest Entities.",
        long_description="We provide bespoke accountancy services to our clients ranging from start-ups to Public Interest Entities. We strive to find the appropriate accounting solutions to enable them to fulfil their statutory requirements whilst enabling them to prepare timely management accounts to support them in managing their business. We hold regularly meetings with our clients, as part of our bespoke services, to explain in detail the management accounts and highlight key issues which will help them in their decision making process and business plans. We provide an important interface between our clients and their strategic stakeholders in respect of all financial matters whenever required.",
        details=[
                "Bookkeeping and accounting required for your company.",
                "Maintaining of accounting records on accounting software.",
                "Preparation of monthly management accounts for review and discussions with management.",
                "Liaise with auditors for finalising of accounts.",
                "Preparation of yearly accounts for submission to the MRA and /or Company Registrar.",
        ]
    ),
    Service(
        path="corporate-finance",
        name="Corporate Finance",
        icon="briefcase",
        short_description="At Abhasa Financial Services, we work closely with our clients to determine any funding requirement for their business growth and/or acquisition of new businesses.",
        long_description="At Abhasa Financial Services, we work closely with our clients to determine any funding requirement for their business growth and/or acquisition of new businesses.  We assist in the preparation of any feasibility studies that may be required, help in identifying the appropriate financial institutions; assist in the negotiation process and the preparation of documents for the application process.",
    ),
    Service(
        path="tax-services",
        icon="percent",
        name="Tax Services",
        short_description="at abhasa financial services, we work closelywith our clients to determine any funding requirement for their business growth and / or acquisition of new businesses.",
        long_description="We assist our clients to be Tax compliant and provide the required support in the computation of Income Tax and VAT returns as well as their filings.  We actively advise our clients in their Tax planning and deal with any queries and/or investigations by the Mauritius Revenue Authority (MRA).",
        details=[
            "Preparation of VAT return for its submission to the MRA.",
            "Preparation and submission of quarterly APS/CPS when applicable.",
            "Preparation of Income Tax computation and submission of tax return as per statutory requirements.",
            "Advice on tax planning and tax disputes.",
        ]
    ),
    Service(
        path="applications",
        icon="check-circle",
        name="Permit & Licence Applications",
        short_description="To start a business in Mauritius, companies need to be aware of the different permits and licenses to apply for pertaining to their business activities.",
        long_description="To start a business in Mauritius, companies need to be aware of the different permits and licenses to apply for pertaining to their business activities. Our team will guide you through every step of the application process in order to get your business up and running.",
    ),
    Service(
        path="it",
        icon="laptop-code",
        name="Information Technology",
        short_description="Our team advises you on the appropriate accountancy software for SME to implement and for more complex businesses we can assist in selecting your ERP solution provider.",
        long_description="Our team advises you on the appropriate accountancy software for SME to implement and for more complex businesses we can assist in selecting your ERP solution provider. We will be the key interface between the service provider and the client to ensure successful implementation.  We can advise on IT structure that will best suit the business needs whether being a local inexpensive backup system or a cloud based solution without the need of investing in servers and other associated hardware.",
    ),
    Service(
        path="payroll",
        icon="money-bill-alt",
        name="Payroll Solutions",
        short_description="Our payroll services include the monthly preparation of payslips, filing of monthly and annual returns; and the preparation of yearly Statement of Emoluments.",
        long_description="Our payroll services include the monthly preparation of payslips, filing of monthly and annual returns; and the preparation of yearly Statement of Emoluments. We also assist owners of businesses and directors in their annual Income Tax filings.",
    ),
    Service(
        path="secretarial-finance",
        icon="users",
        name="Corporate Secretarial Finance",
        short_description="Abhasa Limited provides a full fledge secretarial services to our clients to ensure compliance with the provisions of the Companies Act 2001.",
        long_description="Abhasa Limited provides a full fledge secretarial services to our clients to ensure compliance with the provisions of the Companies Act 2001. Talk to us about your needs and requirements and we will be delighted to assist you.",
        details=[
            "Incorporation of companies.",
            "Maintaining of all statutory registers and certificates.",
            "Filing of all statutory returns.",
            "Provision of a qualified Company Secretary.",
            "Organise Board meetings and Annual Shareholder’s meetings.",
            "Issuing of share certificates, certified extract of resolutions and minutes of meetings.",
        ]
    ),
    Service(
        path="start-ups",
        icon="key",
        name="Advisory Services for Start-Up",
        short_description="We appreciate the difficulties and challenges facing most start-ups and we devote considerable time to our clients in order to ensure that they have the necessary information and advice before registering a new business.",
        long_description="We appreciate the difficulties and challenges facing most start-ups and we devote considerable time to our clients in order to ensure that they have the necessary information and advice before registering a new business.",
        details=[
            "Preparation of business plans.",
            "Permit applications.",
            "Company formations.",
            "Opening of bank accounts and assisting in the setting up of the finance and accounting functions of start-ups.",
        ]
    ),

]