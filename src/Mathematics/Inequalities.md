---
headertext: 11th Mathematics (JEE)
...

# **Inequalities**

Inequalities are algebraic statements which use the symbols $<$, $>$, $\le$, $\ge$.

$$5x+3\ge 10$$
$$x(x-1)<0$$

> **Solution Set:** The set of all values of $x$ satisfying the inequality.

## Some important points
- Any number can be added/subtracted from LHS and RHS.
    $$x+3<0$$
    $$x<-3\tag{subtract $3$}$$
- On multiplying/dividing a **positive number** to both sides, the inequality stays.
    $$5x>50$$
    $$x>10\tag{divide $5$}$$
- On multiplying/dividing a **negative number** to both sides, the inequality inverts.
    $$-x>-2$$
    $$x<2\tag{multiply $-1$}$$


## Linear Inequalities in One Variable

$$3x-2<0$$

These inequalities can be solved easily by following the rules of inequalities.

Example 1
$$3x-2<0$$
$$3x<2$$
$$x<\frac23$$
$$x\in \left(-\infty, \frac23\right)$$

> **When a pair of linear inequalities are given, we take the intersection of the solution sets of both the inequalities.**
> 
> Example 2
> $$\frac{5x}4+\frac{3x}8>\frac{39}8 \text{ and } \frac{2x-1}{12}-\frac{x-1}3<\frac{3x+1}4 $$
> $$\begin{aligned}
> \text{Eqn 1: } &\frac{5x}4+\frac{3x}8>\frac{39}8\\
> &10x+3x>39\\
> &13x>39\\
> &\boxed{x>3}\\
> \text{Eqn 2: } &\frac{2x-1}{12}-\frac{x-1}3<\frac{3x+1}4\\
> &(2x-1)-4(x-1)<3(3x+1)\\
> &2x-1-4x+4<9x+3\\
> &-2x+3<9x+3\\
> &0<11x\\
> &\boxed{x>0}
> \end{aligned}$$
> The intersection of the solutions $x>0$ and $x>3$ is $x>3$.
> 
> $\therefore x\in (3,\infty)$

Example 3
$$2\ge 5x-2\ge 4$$
$$4\ge 5x\ge 6$$
$$\frac45\ge x\ge \frac65$$
$$x\in\left[\frac45,\frac65\right]$$

## Inequalities of Higher Order

We use the **Wavy Curve Method** to solve general inequalities.

Example 4
$$(x-2)(x+1)>0$$


1. **We plot the roots of the LHS on a number line.**
   
   We plot $-1$ and $2$ on the number line.

   ![](/images/2022-06-02-13-30-30.png){ width=500px }

2. **Starting from the right hand side, we check the sign of the expression at that value $x$.**

    When $x>2$, then the value of $(x-2)(x+1)$ will be $+\mathrm{ve}$.

    ![](/images/2022-06-02-13-30-07.png){ width=500px }

3. **Going towards the left, we check the power of the factor.**
     - If the power is odd, **the opposite sign** is indicated on the next interval.
     - If the power is even, **the same sign** is indicated on the next interval.
  
   The factor $(x-2)$ is raised to an odd power ($1$). So the next interval (-1 to 2) will be $-\mathrm{ve}$.

   ![](/images/2022-06-02-13-29-54.png){ width=500px }

4. **Continue till all intervals are marked.**

   The factor $(x+1)$ is raised to an odd power ($1$). So the next interval ($-\infty$ to -1) will be $+\mathrm{ve}$.

    ![](/images/2022-06-02-13-28-57.png){ width=500px }

5. **We create the solution set based on the number line.**

   We want to find all values of $x$ such that $(x-2)(x+1)$ is greater that $0$.

   $\therefore x\in(-\infty, -1)\cup(2, \infty)$

> - To use the Wavy Curve Method, we must convert the inequality such that:
>   - LHS is a polynomial with linear factors.
>   - RHS is 0.
> - The roots themselves are included in the solution only if the sign of inequality is $\ge$ or $\le$.

******

Example 5

$$\frac{3x-1}{x-1}\ge 0$$

![](/images/2022-06-02-14-31-02.png)

$$\boxed{x\in \left(-\infty, \frac13\right] \cup \left(1, \infty\right)}$$

Note that here $\frac13$ is included in the solution set because the sign of the inequality is $\ge$.

However, $1$ is not included, because the factor $(x-1)$ is in the denominator of the expression. When $x=1$, the expression becomes *undefined*.


*****

Example 6
$$\frac{2x-3}{3x-5}\ge3$$

$$\frac{2x-3}{3x-5}-3\ge0$$
$$\frac{2x-3-9x+15}{3x-5}\ge0$$
$$\frac{-7x+12}{3x-5}\ge0$$
$$\frac{7x-12}{3x-5}\le0$$

![](/images/2022-06-02-14-51-38.png)

$$\boxed{x\in\left(\frac53, \frac{12}7\right]}$$