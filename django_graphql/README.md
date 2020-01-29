# Referencias

### Scalars
https://docs.graphene-python.org/en/latest/types/scalars/

### Django + GraphQL + JWT
https://github.com/flavors/django-graphql-jwt

### Apollo Server
https://www.apollographql.com/docs/apollo-server/getting-started/

### Graphene Table of contents
https://docs.graphene-python.org/en/latest/

### Middleware
https://docs.graphene-python.org/en/latest/execution/middleware/

### Introspection
https://docs.graphene-python.org/projects/django/en/latest/introspection/

### Unittests
https://docs.graphene-python.org/projects/django/en/latest/testing/

### Postman
https://learning.getpostman.com/docs/postman/sending-api-requests/graphql/

# SDL sample code

### Simple Query
```
query getActor{
  actor(id: 3){
    id
    name
  }
}
```

### Querying sets
```
query getActor {
  actor(id: 1) {
    id
    name
    movieSet {
      title
      id
      actors {
        edges {
          node {
            name
          }
        }
      }
      year
    }
  }
}
```

### Query a list field
```
query{
  actors{
    pk
    name
    id
  }
}
```

### Query a list with filtering
```
{
  actors(name_Icontains: "") {
    edges {
      node {
        name
        id
      }
    }
  }
}
```

### Mutation
```
mutation{
  createActor(input: {
    name: "Joseph Zamora"
  }){
    actor{
      name
    }
  }
}
```
### Mutation with variables
```
mutation createActor($input: ActorInput!){
  createActor(input: $input){
    actor{
      name
    }
  }
}
```
Add this code to variables section:
```
{
  "input":{
		"name": "Joseph Zamora"
	}
}
```

### Mutation update 
```
mutation{
  updateActor(id:3, input: {
    name: "George Lopez"
  }){
    actor{
      name
    }
  }
}
```
