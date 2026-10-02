from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:

    def chunk_text(self, text, chunk_size=50, chunk_overlap=5):
        """Split document text into smaller chunks."""

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        chunks = splitter.split_text(text)

        return chunks