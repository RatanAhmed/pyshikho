from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from .models import Questions, Learn

PUBLISHER_INDEX = Index('search')
@registry.register_document
class QuestionDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'questions'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Questions # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'description',
        ]

# @registry.register_document
# class LearnDocument(Document):
#     class Index:
#         name = 'learn'
#         settings = {'number_of_shards': 1,
#                     'number_of_replicas': 0}

#     class Django:
#         model = Learn # The model associated with this Document

#         # The fields of the model you want to be indexed in Elasticsearch
#         fields = [
#             'title',
#             'description',
#         ]
  