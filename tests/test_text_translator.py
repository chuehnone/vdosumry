import unittest
from unittest.mock import patch
from vdosumry.llm.ollama import Ollama
from vdosumry.text_translator import TextTranslator


class TestTextTranslator(unittest.TestCase):
    @patch("requests.post")
    def test_translate(self, mock_post):
        # Arrange
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = '{"response": "這是一個測試翻譯"}\n'
        mock_post.return_value = mock_response

        ollama = Ollama(model="llama3.2")
        translator = TextTranslator(target_language="zh-TW", llm=ollama)
        text_to_translate = "This is a test translation."

        # Act
        translated_text = translator.translate(text_to_translate)

        # Assert
        self.assertEqual(translated_text, "這是一個測試翻譯")


if __name__ == "__main__":
    unittest.main()
