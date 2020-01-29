import graphene
from graphene import Schema


# class Character(graphene.ObjectType):
# name = graphene.NonNull(graphene.String)

# def resolver_name(root, info, name):
# return "Hello world"


# class Character(graphene.ObjectType):
# name = graphene.String()

# def resolve_name(root, info, name):
# return "Hello world"


class Character(graphene.ObjectType):
    appears_in = graphene.List(graphene.String)

    @staticmethod
    def resolve_appears_in(root, info):
        return ["Movie1", "Movie2"]


# class Character(graphene.ObjectType):
# appears_in = graphene.List(graphene.NonNull(graphene.String))

schema = Schema(query=Character)

if __name__ == "__main__":
    query_string = "{ appearsIn }"
    result = schema.execute(query_string)
    print(result.data["appears_in"])
