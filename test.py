from dedoc import DedocManager
from dedoc.attachments_extractors import DocxAttachmentsExtractor
from dedoc.converters import DocxConverter
from dedoc.metadata_extractors import DocxMetadataExtractor
from dedoc.readers import DocxReader
from dedoc.structure_constructors import TreeConstructor
from dedoc.structure_extractors import DefaultStructureExtractor
from dedoc.data_structures import DocumentContent

file_path = 'test_files/5342.pdf'
manager = DedocManager()
recognized_data = manager.parse(file_path=file_path)
print(recognized_data.to_api_schema)
# print(recognized_data.content.tables)
