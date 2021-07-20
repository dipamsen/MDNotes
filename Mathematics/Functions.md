# Relations and Functions

## Relations

- Relations are a subset of the **cardinal product of two sets.**

A relation between set $A$ and $B$ can be denoted as:
$$R_{AB} \subseteq \{(x, y) : x \in A, y \in B\}$$

## Functions

- Functions are Relations of whom:

  - Every element of first set should have an image in second set.
  - No $x \in A$ can have more than one image in $B$

## Types of Relations

1. Void Relation

Let $A$ be a set. Then $\phi \subseteq A \times A$ , so it is a relation on $A$.

2. Universal Relation

Let $A$ be a set. Then $A \times A \subseteq A \times A$

3. Identity Relation

Let $A$ be a set. Then the Relation $I_A = \{(a,a) : a \in A\}$

4. Reflexive Relation

A relation $R$ on a set $A$ is said to be reflexive if every element of $A$ is related to itself. The R is reflexive $\Leftrightarrow (a, a) \in R$ for all $a \in A$

> Eg:
> $$A = \{1, 2, 3\}$$
>
> $$R_1=\{(1, 1), (2, 2), (3, 3), (1, 3),(1, 2)\}$$
>
> $R_1$ is reflexive.
>
> $$R_2=\{(1, 1), (2, 2)\}$$
>
> $R_2$ is not reflexive.

---

- Symmetric Relations

A relation $R$ on a set $A$ is symmetric iff:
$$ (a, b) \in R \implies (b, a) \in R$$
for all $a, b \in A$

- Transitive Relations

A relation $R$ on a set $A$ is transitive iff:
$$(a, b) \in R \; \land (b, c) \in R \implies (a, c) \in R$$
for all $a, b, c \in A$

Notes:

- $R_1$ is Symmetric and Transitive $\implies R_1$ is Reflexive.

---

- Equivalence relation:

Iff:

- it is reflexive ($(a, a)$ is present for all $a$)
- it is symmetric ($(a, b)$ implies $(b, a)$)
- it is transitive ($(a, b)$ and $(b, c)$ implies $(a, c)$)

<!-- Triangle Similarity Example -->
