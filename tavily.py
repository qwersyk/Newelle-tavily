from .extensions import NewelleExtension
from .utility.pip import install_module, find_module
from typing import List


class TavilySearchExtension(NewelleExtension):
    name = "Tavily Search"
    id = "tavilysearch"

    def __init__(self, a, b, c) -> None:
        super().__init__(a, b, c)
        # Load essential settings
        self.api_key = self.get_setting("api_key") or ""
        self.search_depth = self.get_setting("search_depth") or "basic"
        self.max_results = self.get_setting("max_results") or 5
        self.include_answer = self.get_setting("include_answer") or "false"
        self.extract_depth = self.get_setting("extract_depth") or "basic"

    def install(self):
        if not find_module("tavily-python"):
            install_module("tavily-python", self.pip_path)

    def get_replace_codeblocks_langs(self) -> list:
        return ["search", "website"]

    def get_extra_settings(self):
        return [
            {
                "key": "api_key",
                "title": "Tavily API Key",
                "description": "Enter your Tavily API key to use the search functionality",
                "type": "entry",
                "default": ""
            },
            {
                "key": "search_depth",
                "title": "Search Depth",
                "description": "The depth of the search. Basic (1 credit) or Advanced (2 credits)",
                "type": "combo",
                "values": [("basic", "Basic"), ("advanced", "Advanced")],
                "default": "basic"
            },
            {
                "key": "include_answer",
                "title": "Include AI Answer",
                "description": "Include an LLM-generated answer to the query",
                "type": "combo",
                "values": [
                    ("false", "No Answer"),
                    ("basic", "Basic Answer"),
                    ("advanced", "Detailed Answer")
                ],
                "default": "false"
            },

            {
                "key": "extract_depth",
                "title": "Extract Depth",
                "description": "The depth of website content extraction. Advanced retrieves more data but costs more credits.",
                "type": "combo",
                "values": [("basic", "Basic"), ("advanced", "Advanced")],
                "default": "basic"
            }
        ]

    def get_additional_prompts(self) -> list:
        return [
            {
                "key": "tavilysearch",
                "setting_name": "tavilysearch",
                "title": "Tavily Search Integration",
                "description": "Enable Tavily Search for retrieving web results.",
                "editable": True,
                "show_in_settings": True,
                "default": True,
                "text": "Use \n```search\nquery\n```\n to perform a web search using Tavily API."
            },
            {
                "key": "tavilywebsite",
                "setting_name": "tavilywebsite",
                "title": "Tavily Website Content",
                "description": "Extract content from websites using Tavily API.",
                "editable": True,
                "show_in_settings": True,
                "default": True,
                "text": "Use \n```website\nURL\n```\n to extract content from a website."
            }
        ]

    def format_content(self, response: dict) -> str:
        """Format the extracted content in a clean, readable way."""
        formatted_content = []

        if not response.get("results"):
            return "No content could be extracted from the website."

        for result in response["results"]:
            if result.get("title"):
                formatted_content.append(f"# {result['title']}\n")
            if result.get("text"):
                formatted_content.append(result["text"])
            if result.get("urls"):
                formatted_content.append("\n## Links:")
                for url in result["urls"]:
                    formatted_content.append(f"- {url}")

        return "\n\n".join(formatted_content)
    def format_website(self, response: dict) -> str:
        """Format the extracted content in a clean, readable way."""
        formatted_content = []
        if not response.get("results"):
            return "No content could be extracted from the website."
        for result in response["results"]:
            if result.get("raw_content"):
                formatted_content.append(result["raw_content"])

        return "\n\n".join(formatted_content)

    def get_answer(self, codeblock: str, lang: str) -> str | None:
        try:
            from tavily import TavilyClient

            if not self.api_key:
                return "Error: Tavily API key not configured. Please set your API key in the extension settings."

            client = TavilyClient(api_key=self.api_key)

            if lang == "website":
                try:
                    url = codeblock.strip()

                    extract_params = {
                        "urls": [url]
                    }

                    response = client.extract(**extract_params)
                    return self.format_website(response)

                except Exception as e:
                    return f"Error extracting website content: {str(e)}"

            # Handle search
            if lang == "search":
                search_params = {
                    "query": codeblock.strip(),
                    "search_depth": self.search_depth,
                    "max_results": int(self.max_results)
                }


                response = client.search(**search_params)

                if not response:
                    return "No results found."

                formatted_results = []

                if "answer" in response and response["answer"]:
                    formatted_results.append(f"AI Answer: {response['answer']}\n")

                if "results" in response and response["results"]:
                    formatted_results.append("Web Results:")
                    for result in response["results"]:
                        url = result.get("url", "URL not found")
                        snippet = result.get("content", "Content not found")
                        formatted_results.append(f"{snippet}\n({url})\n")

                return "\n".join(formatted_results) if formatted_results else "No results found."

        except Exception as e:
            return f"Error: {str(e)}"