## DDE Resource Type

Constrains `schema:additionalType` to require at least one `schema:DefinedTerm` from the DDE `ResourceTypeCode` codelist (`dde:codelist/ResourceTypeCode`).

The DDE vocabulary defines 32 resource types from the DDE spec Table 18: aggregate, application, webApplication, collection, dataset, dataCatalog, geographicDataset, nonGeographicDataset, document, article, thesis, book, poster, webPage, image, map, photograph, explanatoryFigure, initiative, fieldSession, learningResource, guide, model, movie, repository, semanticResource, definedTermSet, series, service, webAPI, software, sound.

This building block is used by `ddeRequired` to enforce DDE resource typing on metadata records.
