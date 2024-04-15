## Query ~##

1 - Quantos alunos estão registados? (inteiro)

```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
select (Count(?s)as ?n)  where {
    ?s a :Aluno .
} 
```

2 - Quantos alunos frequentam o curso "LCC"? (inteiro)

```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select (Count(?s)as ?n)  where {
    ?s  rdf:type :Aluno;
    	:curso "LCC"
} 
```

3 - Que alunos tiveram nota positiva no exame de época normal? (lista ordenada alfabeticamente
por nome com: idAluno, nome, curso, nota do exame);

```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?s ?nome ?curso ?notanormal where {
    ?s  rdf:type :Aluno;
    	:temExame ?exame ;
    	:nome ?nome;
    	:curso ?curso .
    ?exame :exameNormal ?notanormal .
    FILTER((?notanormal > 10)) 
} ORDER by Asc (?nome)
```

4 - Qual a distribuição dos alunos pelas notas do projeto? (lista com: nota e número de alunos que
obtiveram essa nota)

    ```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?notaprojeto (Count(?s)as ?n) where {
    ?s  rdf:type :Aluno ;
    	:projeto ?notaprojeto .
} GROUP BY (?notaprojeto)  ORDER by Desc (?notaprojeto)
```

5 - Quais os alunos mais trabalhadores durante o semestre? (lista ordenada por ordem
decrescente do total: idAluno, nome, curso, total = somatório dos resultados dos TPC)

    ```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?nome ?curso ?notaProjeto WHERE {
      ?aluno a :Aluno;
         :curso ?curso;
         :nome ?nome;
         :idAluno "PG49576";
         :projeto ?notaProjeto .
}

```

6 - Qual a distribuição dos alunos pelos vários cursos? (lista de cursos, ordenada alfabeticamente
por curso, com: curso, número de alunos nesse curso)

    ```sql
PREFIX : <http://rpcw.di.uminho.pt/2024/avaliacao/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?curso (COUNT(?s)as ?nalunos) where {
    ?s  rdf:type :Aluno ;
    	:curso ?curso
} Group by ?curso Order by Asc (?curso)
```

