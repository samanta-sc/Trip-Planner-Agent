import os
from utils.place_info_search import TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            
            attraction_result = self.tavily_search.tavily_search_attractions(place)
            if attraction_result:
                return f"Following are the attractions of {place} as suggested by tavily: {attraction_result}"
        
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            
            restaurants_result = self.tavily_search.tavily_search_restaurants(place)
            if restaurants_result:
                return f"Following are the restaurants of {place} as suggested by tavily: {restaurants_result}"
        
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            
            restaurants_result = self.tavily_search.tavily_search_activity(place)
            if restaurants_result:
                return f"Following are the activities in and around {place} as suggested by tavily: {restaurants_result}"
            
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            
            restaurants_result = self.tavily_search.tavily_search_transportation(place)
            if restaurants_result:
                return f"Following are the modes of transportation available in {place} as suggested by tavily: {restaurants_result}"
    
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]