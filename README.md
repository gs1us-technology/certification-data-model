# certification-data-model

This repository contains a data model to share certificaion summary information between trading partners.

# Contents

The ```docs``` folder contains the json schema for the compacted (JSON) format document as well as the JSON-LD context for
expanding into globally defined terms.

The ```examples``` folder contains a compact form sample certification report, and the expanded (and then compacted)
version. You can get the equivalent to this by entering the ```jsonCertSample.json``` file into [https://json-ld.org/playground/]
and selecting the compact version.

The script ```validate.py``` validates the sample file against the schema and the expands and compacts it an ensures
its matching (no data lost).


# Data Element Details

| Header / Object | Add to web voc | Req/Cond/Opt | JSON Property Shorthand | JSON-LD Property Name | Data Type | Description | Example | Comments |
|-----------------|----------------|--------------|--------------------------|-----------------------|-----------|-------------|---------|----------|
| Header | X | 🟥 R | issueDate | [gs1:x/issueDate](https://gs1.org/voc/x/issueDate) | [xsd:date](http://www.w3.org/2001/XMLSchema#date) | First date of validity for the certification | 2025-06-30 | |
|  | X | 🟩 O | issuer | [gs1:x/issuer](https://gs1.org/voc/x/issuer) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | GLN or other identifier of document creator | "Certification Report Generator Entity" | |
|  |  | 🟥 R | @context | `@context` | URI | Must point to the cert_context.json file | `"@context": "https://gs1us-technology.github.io/certification-data-model/cert_context.json"` | |
|  |  | 🟥 R | $schema | N/A | URI | Must point to the schema for the JSON shorthand | `"$schema": "https://gs1us-technology.github.io/certification-data-model/cert_schema.json"` | |
|  |  | 🟥 R | id | [rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject) | URI | A globally unique URI describing this certification report | [Sample Report](https://gs1us-technology.github.io/examples/jsonCertSample.json) | |
|  | X | 🟥 R | type | [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | N/A | MUST contain `"CertificationReport"` (see [gs1:x/CertificationReport](https://gs1.org/voc/x/CertificationReport)) | | |
| Object |  | 🟥 R | products | [gs1:x/products](https://gs1.org/voc/x/products) | [Product](https://ref.gs1.org/voc/Product) | A list of one or more products | | |
|  |  | 🟥 R | id | [rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject) | URI | Unique GS1 Digital Link URI for product | `"https://id.gs1.org/01/00123456789128/10/ABCDBatch"` | |
|  |  | 🟥 R | type | [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | N/A | MUST contain `"Product"` (see [gs1:Product](https://ref.gs1.org/voc/Product)) | | |
|  |  | 🟥 R | gtin | [gs1:gtin](https://ref.gs1.org/voc/gtin) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | GTIN (14-digit GS1 Key) | 00123456789012 | |
|  | X | 🟩 O | additionalTradeItemId | [gs1:x/productID](https://ref.gs1.org/voc/x/productID) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Product ID in addition to GTIN (ASIN, SKU, etc.) | "B07P54S890" | Mirrors `additionalOrganizationalID` |
|  |  | 🟩 O | name | [gs1:productName](https://ref.gs1.org/voc/productName) | [rdf:langString](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString) | Short consumer-friendly product name | Short Receipt Desc ABC | |
|  |  | 🟩 O | description | [gs1:productDescription](https://ref.gs1.org/voc/productDescription) | [rdf:langString](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString) | Brand/descriptive product text | Brand Product Description ABC | |
| Object |  | 🟥 R | certificationInfo | [gs1:certification](https://ref.gs1.org/voc/certification) | [CertificationDetails](https://ref.gs1.org/voc/CertificationDetails) | Certification details for product/org/place | N/A | |
|  |  | 🟥 R | id | [rdf:subject](http://www.w3.org/1999/02/22-rdf-syntax-ns#subject) | URI | Globally unique cert URI | [Example](http://www.example.com/certid=2342342) | |
|  |  | 🟥 R | type | [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | N/A | MUST contain `"CertificationDetails"` (see [gs1:CertificationDetails](https://ref.gs1.org/voc/CertificationDetails)) | | |
|  |  | 🟥 R | agency | [gs1:certificationAgency](https://ref.gs1.org/voc/certificationAgency) | [rdf:langString](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString) | Name of certifying organisation | "TCO Development" | |
|  | X | 🟥 R | program | [gs1:x/certificationProgram](https://ref.gs1.org/voc/x/certificationProgram) | [rdf:langString](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString) | Certification program name | TCO Certified | |
|  |  | 🟩 O | certificateId | [gs1:certificationIdentification](https://ref.gs1.org/voc/certificationIdentification) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Vendor-specific cert ID | AB1234567 | |
|  |  | 🟩 O | endDate | [gs1:certificationEndDate](https://ref.gs1.org/voc/certificationEndDate) | [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Expiry date of cert | 2026-05-17 or null | |
|  |  | 🟥 R | standard | [gs1:certificationStandard](https://ref.gs1.org/voc/certificationStandard) | [rdf:langString](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString) | Certification standard/version | "GRS 4.0" | Needs improved definition |
|  |  | 🟥 R | status | [gs1:certificationStatus](https://ref.gs1.org/voc/certificationStatus) | [CertificationStatus](https://ref.gs1.org/voc/CertificationStatus) | Certification status (active/inactive) | ACTIVE | Align with endDate |
|  |  | 🟩 O | level | [gs1:certificationValue](https://ref.gs1.org/voc/certificationValue) | [rdf:langString](http://www.w3.org/1999/02/22-rdf-syntax-ns#langString) | Cert level/tier | Silver | Rename `value` → `level` |
|  |  | 🟩 O | agencyURL | https://ref.gs1.org/voc/certificationAgencyURL | [Organization](https://ref.gs1.org/voc/Organization) | URL of certifying agency | [TCO Certified](https://tcocertified.com/) | |
|  |  | 🟩 O | auditDate | [gs1:certificationAuditDate](https://ref.gs1.org/voc/certificationAuditDate) | [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Audit completion date | 2026-05-17 | Not mapped in pilot |
|  |  | 🟩 O | startDate | [gs1:certificationStartDate](https://ref.gs1.org/voc/certificationStartDate) | [xsd:date](http://www.w3.org/2001/XMLSchema#date) | First validity date | 2026-05-17 | |
|  |  | 🟩 O | certificationURI | [gs1:certificationURI](https://ref.gs1.org/voc/certificationURI) | [xsd:anyURI](https://www.w3.org/2001/XMLSchema#anyURI) | Link to agency cert record | https://tcocertified.com/certID/abc780123 | Not mapped in pilot |
|  |  | 🟩 O | initialCertificationDate | [gs1:initialCertificationDate](https://ref.gs1.org/voc/initialCertificationDate) | [xsd:date](http://www.w3.org/2001/XMLSchema#date) | Original issue date | 2026-05-17 | Not mapped in pilot |
| Object | X | 🟧 C | targetCountries | [gs1:x/certificationApplicableCountries](https://gs1.org/voc/x/certificationApplicableCountries) | [Country](https://ref.gs1.org/voc/Country) | Countries where certification applies | N/A | Issue #9 |
|  |  | 🟥 R | countryCode | [gs1:countryCode](https://ref.gs1.org/voc/countryCode) | [xsd:string](http://www.w3.org/2001/XMLSchema#string) | ISO 3166-1 numeric code | "840" (US), "124" (CA) | |
|  |  | 🟥 R | type | [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | N/A | MUST contain `"Country"` (see [gs1:Country](https://ref.gs1.org/voc/Country)) | | |
