from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from . import serializers
from . import models
from .permissions import IsLinkOwner, IsSubTopicLinkOwner, IsSubTopicOwner, IsTopicOwner, IsCurationOwner

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'subjects': reverse('subject-list', request=request, format=format),
        'curations': reverse('curation-list', request=request, format=format)
    })
class SubjectList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SubjectDetail(mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

    def retrieve(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CurationList(mixins.ListModelMixin,
					mixins.CreateModelMixin,
                	generics.GenericAPIView):

	queryset = models.Curation.objects.all()
	serializer_class = serializers.CurationSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCurationOwner]

	def get_queryset(self):
		"""
		Optionally restricts the returned purchases to a given user,
		by filtering against a `username` query parameter in the URL.
		"""
		queryset = models.Curation.objects.all()
		subject = self.request.query_params.get('subject')
		if subject is not None:
			queryset = queryset.filter(subject=subject)
		return queryset

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
	
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class CurationDetail(mixins.RetrieveModelMixin,
					mixins.DestroyModelMixin,
					mixins.UpdateModelMixin,
					generics.GenericAPIView):

	queryset = models.Curation.objects.all()
	serializer_class = serializers.CurationSerializer

	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCurationOwner]

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)
	
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	def delete(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)


class TopicCreate(mixins.CreateModelMixin, generics.GenericAPIView):

	queryset = models.Topic.objects.all()
	serializer_class = serializers.TopicSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTopicOwner]

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class TopicDetail(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
	queryset = models.Topic.objects.all()
	serializer_class = serializers.TopicSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTopicOwner]

	def delete(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)
	
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)


class LinkCreate(mixins.CreateModelMixin, generics.GenericAPIView):

	queryset = models.Link.objects.all()
	serializer_class = serializers.LinkSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsLinkOwner]

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class LinkDetail(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
	queryset = models.Link.objects.all()
	serializer_class = serializers.LinkSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsLinkOwner]

	def delete(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)
	
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

class SubTopicCreate(mixins.CreateModelMixin, generics.GenericAPIView):

	queryset = models.SubTopic.objects.all()
	serializer_class = serializers.SubTopicSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSubTopicOwner]


	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class SubTopicDetail(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
	queryset = models.SubTopic.objects.all()
	serializer_class = serializers.SubTopicSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSubTopicOwner]

	def delete(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)
	
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
class SubTopicLinkCreate(mixins.CreateModelMixin, generics.GenericAPIView):

	queryset = models.SubTopicLink.objects.all()
	serializer_class = serializers.SubTopicLinkSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSubTopicLinkOwner]

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class SubTopicLinkDetail(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
	queryset = models.SubTopicLink.objects.all()
	serializer_class = serializers.SubTopicLinkSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSubTopicLinkOwner]

	def delete(self, request, *args, **kwargs):
		return super().destroy(request, *args, **kwargs)
	
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)