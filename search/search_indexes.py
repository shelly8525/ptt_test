from haystack import indexes
from search.models import Company1

class Company1Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    push = indexes.CharField(model_attr='push')
    title = indexes.CharField(model_attr='title')
    date = indexes.CharField(model_attr='date', null=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Company1

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
