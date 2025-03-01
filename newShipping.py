class newShipping:
    def completar_formulario(self):
        self.datos = {
            "shipping_instructions": "EXPO 57869",
            "company_name": "NIBIRU LLC",
            "set_point_temperature": "-24° C",
            "contract_number": "",
            "description_of_goods": "ILLEX ARGENTINUS SQUID WHOLE ROUND (ILLEX ARGENTINUS)",
            "ncm": "",
            "max_net_weight": "27,000 kg / per container",
            "max_gross_weight": "28,000 kg / per container",
            "number_of_sets": "1 set of documents per operation (not per container)",
            "documents_required": {
                "bill_of_lading": "Telex Release",
                "cert_of_origin": "(1 ORIGINAL + 3 COPIES)",
                "health_certificate": "(1 ORIGINAL + 3 COPIES)",
                "packing_list": "(1 ORIGINAL + 3 COPIES)",
                "commercial_invoice": "(1 ORIGINAL + 3 COPIES)",
                "catch_certificate": "(1 ORIGINAL)",
                "official_weight_sheet": "VGM"
            },
            "freight_prepaid_or_collect": "PREPAID",
            "who_pays_freight": "NIBIRU LLC",
            "bl_release": "TELEX RELEASE",
            "consignee_bl": {
                "name": "MASTER OF F/V “NO.7 CHOKYU MARU”",
                "address": "C/O Serex Maritimos, SL",
                "phone": "928338248",
                "fax": "928468642",
                "email": "administracion@serexmaritimos.com"
            },
            "notify_bl": {
                "name": "MASTER OF F/V “NO.7 CHOKYU MARU”",
                "address": "C/O Serex Maritimos, SL",
                "phone": "928338248",
                "fax": "928468642",
                "email": "administracion@serexmaritimos.com"
            },
            "final_destination": "PORT OF DISCHARGE LAS PALMAS, SPAIN",
            "origin_certificate_consignee": {
                "name": "MASTER OF F/V “NO.7 CHOKYU MARU”",
                "address": "C/O Serex Maritimos, SL"
            },
            "health_certificate_consignee": {
                "name": "MASTER OF F/V “NO.7 CHOKYU MARU”",
                "address": "C/O Serex Maritimos, SL",
                "phone": "928338248",
                "fax": "928468642",
                "email": "administracion@serexmaritimos.com"
            },
            "packing_list_consignee": {
                "name": "Fishing Eight Inc",
                "address": "406 Amapola Ave Suite 235, Torrance, CA 902501",
                "phone": "(310)988-1588",
                "fax": "(310)988-1589"
            },
            "commercial_invoice_consignee": {
                "name": "NIBIRU LLC",
                "address": "140 South Cache Street, Jackson, Wyoming - USA",
                "ein": "85-3423224"
            },
            "incoterm": "CFR",
            "delivery_of_documents": "TBC",
            "comments": [
                "THERMOGRAPH (Se debe colocar al menos un Termógrafo por contenedor). ITS NUMBER SHALL BE SHOWN ON B/L AND PACKING LIST.",
                "PACKING LIST SHALL SHOW LOT NUMBERS AND DATES",
                "CONTROL DE CARGA. Tomar fotos donde se observe claramente todos los detalles del contenedor, producto, etiqueta, termógrafo y precinto.",
                "En la manera de lo posible, favor de solicitar al personal de estiba que se coloquen los barbijos y guantes correctamente al momento de filmar y tomar fotos."
            ]
        }

        self.validar_formulario()

    def validar_formulario(self):
        required_fields = ["company_name", "set_point_temperature", "description_of_goods", 
                           "max_net_weight", "max_gross_weight", "number_of_sets", 
                           "documents_required", "freight_prepaid_or_collect", 
                           "who_pays_freight", "bl_release", "consignee_bl", 
                           "notify_bl", "final_destination", "origin_certificate_consignee", 
                           "health_certificate_consignee", "packing_list_consignee", 
                           "commercial_invoice_consignee", "incoterm"]

        for field in required_fields:
            if field not in self.datos or not self.datos[field]:
                raise ValueError(f"Required field '{field}' is missing or empty")


