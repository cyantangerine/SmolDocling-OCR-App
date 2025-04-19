# %%
%env ALL_PROXY=http://127.0.0.1:7856
%env HTTP_PROXY=http://127.0.0.1:7856
%env HTTPS_PROXY=http://127.0.0.1:7856

# %%
from docling.document_converter import DocumentConverter
source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
converter = DocumentConverter(
    format_options=[
        InputFormat
    ]
)
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
# %%
from docling_core.types.doc import ImageRefMode
with open("./1.md", 'w') as f:
    f.write(result.document.export_to_markdown(image_mode=ImageRefMode.EMBEDDED)
)
