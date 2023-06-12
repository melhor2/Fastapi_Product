from models.Supplier import Supplier as SupplierModel

class SupplierService():
    def __init__(self,db):
        self.db = db

    def get_supplier(self):
        result = self.db.query(SupplierModel).all()
        return result
    

    def get_supplier_for_id(self,id:int):
        result = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        return result
    
    def create_supplier(self,supplier:SupplierModel):
        new_supplier = SupplierModel(
            name = supplier.name.upper(),
            address = supplier.address.upper(),
            phone = supplier.phone.upper(),
            email = supplier.email.upper()
        )
        self.db.add(new_supplier)
        self.db.commit()
        self.db.refresh
        return
    

    def update_supplier(self,data:SupplierModel):
        supplier = self.db.query(SupplierModel).filter(SupplierModel.id == data.id).first()
        supplier.name = data.name
        supplier.address = data.address
        supplier.phone = data.phone
        supplier.email = data.email
        self.db.commit()
        return
    

    def delete_supplier(self,id:int):
        self.db.query(SupplierModel).filter(SupplierModel.id == id).delete()
        self.db.commit()
        