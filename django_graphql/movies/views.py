from django.http import HttpResponse
from graphene import ObjectType, String, Schema, Int, Field

from movies.models import Actor


class ActorType(ObjectType):
    detail = String()


class Query(ObjectType):
    actor = Field(ActorType, name=String(), pk=Int())

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    @staticmethod
    def resolve_actor(root, info, **kwargs):
        pk = kwargs.get("pk")
        name = kwargs.get("name")
        if pk:
            obj = Actor.objects.get(pk=pk)
        elif name:
            obj = Actor.objects.get(name=name)
        else:
            return "Object not found"
        return {"detail": f"Actor {obj.name} found with ID {obj.id}"}


schema = Schema(query=Query)


def get_actor(request):
    response = schema.execute(request.body.decode())
    return HttpResponse(response.data["actor"]["detail"])
