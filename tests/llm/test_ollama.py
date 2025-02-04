import unittest
from unittest.mock import patch
from vdosumry.llm.ollama import Ollama


class TestOllama(unittest.TestCase):
    @patch("requests.post")
    def test_generate(self, mock_post):
        # Arrange
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = """{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.228823Z","response":"Certainly","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.27759Z","response":"!","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.326522Z","response":" Here","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.37531Z","response":"'s","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.42458Z","response":" a","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.47351Z","response":" one","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.522674Z","response":"-line","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.571723Z","response":" response","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.620825Z","response":" to","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.669905Z","response":" your","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.719246Z","response":" test","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.768613Z","response":" prompt","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.81814Z","response":":","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.867687Z","response":" \\"","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.91706Z","response":"Thank","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:50.966376Z","response":" you","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.015651Z","response":" for","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.065151Z","response":" the","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.114414Z","response":" prompt","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.163786Z","response":";","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.213415Z","response":" how","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.262605Z","response":" can","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.311742Z","response":" I","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.360958Z","response":" assist","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.410212Z","response":" you","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.459625Z","response":" further","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.508837Z","response":"?\\"","done":false}
{"model":"phi4:latest","created_at":"2025-02-04T01:24:51.558394Z","response":"","done":true,"done_reason":"stop","context":[100264,882,100266,198,2028,374,264,1296,10137,13,21335,757,220,16,1584,2077,13,100265,198,100264,78191,100266,198,96556,0,5810,596,264,832,8614,2077,311,701,1296,10137,25,330,13359,499,369,279,10137,26,1268,649,358,7945,499,4726,7673],"total_duration":1766067375,"load_duration":23849000,"prompt_eval_count":23,"prompt_eval_duration":411000000,"eval_count":28,"eval_duration":1330000000}
"""
        mock_post.return_value = mock_response

        ollama = Ollama()
        ollama.set_default_model("phi4:latest")
        prompt = "This is a test prompt. Give me 1 line response."

        # Act
        generated_text = ollama.generate(prompt)

        # Assert
        self.assertEqual(
            generated_text,
            'Certainly! Here\'s a one-line response to your test prompt: "Thank you for the prompt; how can I assist you further?"',
        )

    @patch("requests.get")
    def test_list(self, mock_get):
        # Arrange
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.text = '{"models":[{"name":"deepseek-r1:14b","model":"deepseek-r1:14b","modified_at":"2025-01-25T11:37:05.712056892+08:00","size":8988112040,"digest":"ea35dfe18182f635ee2b214ea30b7520fe1ada68da018f8b395b444b662d4f1a","details":{"parent_model":"","format":"gguf","family":"qwen2","families":["qwen2"],"parameter_size":"14.8B","quantization_level":"Q4_K_M"}},{"name":"phi4:latest","model":"phi4:latest","modified_at":"2025-01-11T12:01:21.362712793+08:00","size":9053116391,"digest":"ac896e5b8b34a1f4efa7b14d7520725140d5512484457fab45d2a4ea14c69dba","details":{"parent_model":"","format":"gguf","family":"phi3","families":["phi3"],"parameter_size":"14.7B","quantization_level":"Q4_K_M"}}]}'
        mock_get.return_value = mock_response

        ollama = Ollama()

        # Act
        models = ollama.list()

        # Assert
        self.assertEqual(models, ["deepseek-r1:14b", "phi4:latest"])


if __name__ == "__main__":
    unittest.main()
