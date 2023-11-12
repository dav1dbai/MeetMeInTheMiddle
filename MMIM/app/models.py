from decouple import config
import json
import cohere

co = cohere.Client(config('CO_API_KEY'))

def getResponse(prompt):
    response = co.chat(
        model = 'command',
        message = prompt,
        temperature = 0.3,
        citation_quality = 'accurate',
        connectors =[{"id": "web-search"}]
    )
    return response

from django.db import models


# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " at " + self.location
    
    def getLocation(self):
        location = self.location
        ulocation = "University of Southern California, Los Angeles"
        return ulocation
    
    def getRec(self):
        location = self.location
        ulocation = self.getLocation()
        print(ulocation)
        print(location)
        prompt = '''
            Find a location equidistant between {} and {}. 
            List some attractions and activities there along with a brief description.
            Include sources. 
            '''
        prompt = prompt.format(ulocation, location)
        print(prompt)
        streaming_gens = getResponse(prompt)

        json_obj = {
            "text": streaming_gens.text,
            "documents": streaming_gens.documents
        }
        return json_obj
