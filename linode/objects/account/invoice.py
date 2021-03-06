from linode.objects import Base, Property

class Invoice(Base):
    api_name = 'invoices'
    api_endpoint = "/account/invoices/{id}"

    properties = {
        "id": Property(identifier=True),
        "label": Property(),
        "date": Property(is_datetime=True),
        "total": Property(),
    }
