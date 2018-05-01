# Core
Python 3.6.4

Django 2.0.4

## Set virtualenvwrapper
`mkvirtualenv graphql-with-django --python=/usr/local/bin/python3.6z`

## Installation and running
`pip install requirements.txt`

`./manage migrate`

`./manage runserver 0.0.0.0:8000`

## Usage
go to `http://localhost:8000/graphql/`

#### Mutations

```
mutation {
  createAuthor(
    firstName:"John",
    lastName:"Smith",
    email:"john@smith.com",
  )
}
```

```
mutation {
  createPublisher(
    name:"Helioos",
    address:"Grunwaldzka 999",
    city:"Gdansk",
    stateProvince:"Pomorskie",
    country:"Poland",
    website:"publisher@test.pl"
  )
}
```

```
mutation {
  createBook(
    title:"Book title",
    publicationDate:"2000-01-01",
    publisherId:1,
    authors:[1],
  )
}
```

```
mutation {
  deleteAuthor(id:1)
}
```

```
mutation {
  deletePublisher(id:1)
}
```

#### Queries
```
query {
  allBooks {
    title,
    authors {
      firstName,
      lastName,
      email
    },
    publisher {
      name,
      address,
      city,
      stateProvince,
      country,
      website,
    },
   publicationDate 
  }
}
```

```
query {
  allAuthors {
    firstName,
    lastName,
    email,
  }
}
```

```
query {
  allPublishers {
    name,
    address,
    city,
    stateProvince,
    country,
    website,
  }
}
```

```
query {
  publisherById(id:1) {
    name,
    address,
    city,
    stateProvince,
    country,
    website,
  }
}
```

```
query {
  authorById(id:1) {
    firstName,
    lastName,
    email,
  }
}
```
