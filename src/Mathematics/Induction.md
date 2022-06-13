---
headertext: 11th Mathematics (JEE)
...

# **Mathematical Induction**

Mathematical Induction is a principle which is used to prove a proposition $P$ to be true for all natural numbers $n$.

## Steps to Prove a statement

1. **Base Case:** Prove that $P(1)$ is true.
2. **Inductive Step:** Prove that if $P(k)$ is true, then $P(k+1)$ must also be true.

In this way, we end up proving the statement for all natural numbers $n = 1, 2, 3, \cdots$

## Example 1: Sum of Natural Numbers

**Question: Prove that the sum of the first $n$ natural numbers is equal to $\displaystyle \frac{n(n+1)}{2}.$**

**Proof**

$$P(n): 1+2+3+\cdots+n=\frac{n(n+1)}2$$

For $n=1$,

$$\begin{aligned}&\text{ LHS} = 1\\&\text{ RHS} = \frac{1(2)}2=1\end{aligned}$$

$\therefore P(1)$ is true.

Let $P(n)$ be true for $n=k$.

$$
P(k):1+2+3+\cdots+k=\frac{k(k+1)}2\tag{1}
$$

We need to prove that $P(n)$ is also true for $n=k+1$,

$$
P(k+1):1+2+3+\cdots+k+k+1=\frac{(k+1)(k+2)}2
$$

$$
\begin{aligned}\text{LHS}&=\boxed{1+2+3+\cdots+k}+k+1\\
&=\frac{k(k+1)}2+k+1 &\text{(Substituting 1)}\\
&=\frac{k(k+1)+2(k+1)}{2}\\
&=\frac{(k+1)(k+2)}2\\
&=\text{RHS}
\end{aligned}
$$

$\therefore P(k+1)$ is true whenever $P(k)$ is true.

Hence, from the principle of mathematical induction, $P(n)$ is true for all $n\in N$.

## Example 2

**Question: Prove that $\displaystyle1\cdot 3+2\cdot 3^2+3\cdot 3^3+\cdots+n\cdot 3^n=\frac{(2n-1)3^{n+1}+3}4$**

**Proof**

$$P(n): 1\cdot 3+2\cdot 3^2+3\cdot 3^3+\cdots+n\cdot 3^n=\frac{(2n-1)3^{n+1}+3}4$$

For $n=1$,

$$\begin{aligned}&\text{ LHS} = 3\\&\text{ RHS} = \frac{1(3^2)+3}4=\frac{12}4=3\end{aligned}$$

$\therefore P(1)$ is true.

Let $P(n)$ be true for $n=k$.

$$
P(k):1\cdot 3+2\cdot 3^2+3\cdot 3^3+\cdots+k\cdot 3^k=\frac{(2k-1)3^{k+1}+3}4\tag{1}
$$

We need to prove that $P(n)$ is also true for $n=k+1$,

$$
\begin{aligned}
P(k+1):1\cdot 3+2\cdot 3^2+3\cdot 3^3+\cdots+k\cdot 3^k+(k+1)3^{k+1}&=\frac{(2(k+1)-1)3^{(k+1)+1}+3}4\\
&=\frac{(2k+1)3^{k+2}+3}4
\end{aligned}
$$

$$
\begin{aligned}\text{LHS}&=\boxed{1\cdot 3+2\cdot 3^2+3\cdot 3^3+\cdots+k\cdot 3^k}+(k+1)\cdot 3^{k+1}\\
&=\frac{(2k-1)3^{k+1}+3}4+3^{k+1}(k+1) &\text{(Substituting 1)}\\
&=\frac{3^{k+1}(2k-1)+3+3^{k+1}\cdot 4(k+1)}4\\
&=\frac{3^{k+1}(2k-1+4(k+1))+3}4\\
&=\frac{3^{k+1}(6k+3)+3}4\\
&=\frac{3^{k+1}\cdot 3(2k+1)+3}4\\
&=\frac{3^{k+2}(2k+1)+3}4\\
&=\text{RHS}
\end{aligned}
$$

$\therefore P(k+1)$ is true whenever $P(k)$ is true.

Hence, from the principle of mathematical induction, $P(n)$ is true for all $n\in N$.

## Example 3

**Question: Prove that $n(n+1)(n+5)$ is a multiple of 3 for all $n\in N$.**

**Proof**

$$P(n): n(n+1)(n+5)=3m, m\in Z$$

For $n=1$,

$$\begin{aligned}n(n+1)(n+5)&=1\cdot 2\cdot 6\\&=12=3\times 4\end{aligned}$$

$\therefore P(1)$ is true.

Let $P(n)$ be true for $n=k$.

$$
P(k):k(k+1)(k+5)=3m, m\in Z\tag{1}
$$

We need to prove that $P(n)$ is also true for $n=k+1$,

$$
P(k+1):(k+1)(k+2)(k+6)=3q, q\in Z\\
$$

$$
\begin{aligned}
&= (k+1)(k+2)(k+6)\\
&= (k+1)(k^2+8k+12)\\
&= (k+1)\left((k^2+5k)+(3k+12)\right)\\
&= (k+1)(k^2+5k) + (k+1)(3k+12)\\
&= \boxed{k(k+1)(k+5)} + 3(k+1)(k+4)\\
&= 3m + 3(k+1)(k+4)\\
&= 3\left(m+(k+1)(k+4)\right)\\
&= 3q
\end{aligned}
$$

$\therefore P(k+1)$ is true whenever $P(k)$ is true.

Hence, from the principle of mathematical induction, $P(n)$ is true for all $n\in N$.
