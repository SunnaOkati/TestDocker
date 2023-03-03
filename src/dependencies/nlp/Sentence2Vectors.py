from sentence_transformers import SentenceTransformer


class Sentence2Vector:
    def __init__(self, model_path,
                 model: str = ""):
        try:
            self._sent_2_vec = SentenceTransformer(model_path)
        except:
            # Handling missing model by loading and saving a default modal for future runs
            self._sent_2_vec = SentenceTransformer(model)
            self._sent_2_vec.save(model_path)

    def encode(self, sentences):
        return self._sent_2_vec.encode(sentences).tolist()

    def get_embedding_dimensions(self):
        self._sent_2_vec.get_sentence_embedding_dimension()
