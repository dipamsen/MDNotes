---
headertext: 11th Mathematics (JEE)
...

# **Trigonometry**

## Degree Measurement of Angles

Usually, we measure angles in degrees, where $\gdef\cosec{\mathrm{cosec}}360\degree$ is one complete rotation.

$$1\degree = 60'$$
$$1' = 60''$$

## Radian Measurement of Angles

Radians is another unit for measuring angles, where a complete rotation is marked as $2\pi$ radians.
$$360\degree=2\pi$$

![Some angles in Degrees and Radians](/images/2022-05-27-23-37-39.png)

> - A unit circle is a circle with radius 1 unit.
> - The unit 'radian' is often omitted while writing radian angles.

## Definition

**The angle subtended at the centre by an arc of length $x$ in a unit circle is $x$ rad.**

![Definition](/images/2022-05-27-23-44-19.png){ width=340px }

![Illustration](/images/2022-05-28-00-05-17.png)

$$\boxed{\text{Radian measure} = \frac{\text{Arc length}}{\text{Radius}}}$$

## Degree-Radian Conversion

$$180\degree = \pi$$
$$1 \text{ radian} = \frac {180\degree}\pi=57\degree 16'$$
$$1\degree = \frac \pi{180}=0.01746 \text{ radian}$$

$$\boxed{\text{Radian measure} = \frac\pi{180}\times \text{Degree measure}}$$
$$\boxed{\text{Degree measure} = \frac{180}\pi\times \text{Radian measure}}$$

## Trigonometric Functions

(See Figure 4)

$$
\boxed{\begin{aligned}\sin \theta = \text {The \textbf{y-coordinate} of the point on the unit circle}\\
\cos \theta = \text {The \textbf{x-coordinate} of the point on the unit circle}\end{aligned}}
$$

![Trigonometric Functions in a unit circle](/images/2022-05-28-00-53-41.png)

**Quadrantal Angles:** Integral multiples of $\frac\pi2$

![](/images/2022-05-28-10-49-17.png)

### Value of 0

$\sin\theta$ is 0 for the values $\theta = 0, \pi, 2\pi, \cdots$

$\cos\theta$ is 0 for the values $\displaystyle\theta = \frac\pi2, 3\frac\pi2, \cdots$

$$
\left.\begin{aligned}
\therefore \sin\theta &=0\implies \theta = n\pi\\
\cos\theta &=0\implies \theta = (2n+1)\frac\pi2
\end{aligned}\qquad\right\rbrace n\in Z
$$

### Other Trigonometric Functions

$$\tan x = \frac {\sin x}{\cos x}$$
$$\cot x = \frac {\cos x}{\sin x}$$
$$\cosec\ x = \frac {1}{\sin x}$$
$$\sec x = \frac {1}{\cos x}$$

### Pythagorean Identities

$$\sin^2\theta+\cos^2\theta=1 $$
$$1+\tan^2\theta=\sec^2\theta $$
$$1+\cot^2\theta=\cosec^2\theta $$

## Sign of Trigonometric Functions

### Negative Angle

From the unit circle, we can determine the value of functions for a negative angle.

![Negative Angle](/images/2022-05-28-01-15-34.png){ width=320px }

We can see that $\sin x=b; \cos x=a$

For negative value of $x$ (Figure 5), _the x coordinate remains unchanged, while the y coordinate becomes negative._

$$\cos (-x)=\cos x$$
$$\sin (-x)=-\sin x$$

### Sign in different Quadrants

**Quadrant 1:** $a$ and $b$ are both positive \
**Quadrant 2:** $a$ is negative and $b$ is positive \
**Quadrant 3:** $a$ and $b$ are both negative \
**Quadrant 4:** $a$ is positive and $b$ is negative

From the signs of $\sin x$ and $\cos x$, we can find out the signs of all other trigonometric functions.

![Signs of Trigonometric Functions](/images/2022-05-28-11-05-09.png){ width=420px }

## Domain and Range

### $\sin x$

$$\text{Domain} = R$$
$$\text{Range} = [-1, 1]$$

### $\cos x$

$$\text{Domain} = R$$
$$\text{Range} = [-1, 1]$$

### $\mathrm{cosec} \text{ } x$

$$\text{Domain} = \{x:x\in R; x\ne n\pi, n\in Z\}$$
$$\text{Range} = (-\infty, -1] \cup [1, \infty)$$

### $\sec x$

$$\text{Domain} = \{x:x\in R; x\ne (2n+1)\frac\pi2, n\in Z\}$$
$$\text{Range} = (-\infty, -1] \cup [1, \infty)$$

### $\tan x$

$$\text{Domain} = \{x:x\in R; x\ne (2n+1)\frac\pi2, n\in Z\}$$
$$\text{Range} = R$$

### $\cot x$

$$\text{Domain} = \{x:x\in R; x\ne n\pi, n\in Z\}$$
$$\text{Range} = R$$

![Graphs of Trigonometric Functions](/images/2022-05-28-11-31-43.png)

<!-- ![Graphs of Trigonometric Functions](/images/2022-05-28-11-32-43.png) -->

## Trigonometric Identities

- **Negative Angle\***

1. $\sin (-a)=-\sin a$
2. $\cos (-a)=\cos a$
3. $\tan (-a)=-\tan a$

- **Sum or Difference of Angles**

4. $\sin (a+b) = \sin a\cos b + \cos a\sin b$
5. $\sin (a-b) = \sin a\cos b - \cos a\sin b$
6. $\cos (a+b) = \cos a\cos b - \sin a\sin b$
7. $\cos (a-b) = \cos a\cos b + \sin a\sin b$
8. $\displaystyle\tan (a+b) = \frac{\tan a + \tan b}{1-\tan a \tan b}$

9. $\displaystyle\tan (a-b) = \frac{\tan a - \tan b}{1+\tan a \tan b}$
10. $\displaystyle\cot (a+b) = \frac{\cot a\cot b -1}{\cot b + \cot a}$
11. $\displaystyle\cot (a-b) = \frac{\cot a\cot b +1}{\cot b - \cot a}$

- **Multiples of $\frac\pi2$\***

12. $\displaystyle\sin \left(\frac\pi2-x\right) = \cos x$

13. $\displaystyle\sin \left(\frac\pi2+x\right) = -\cos x$
14. $\displaystyle\sin (\pi-x) = \sin x$
15. $\displaystyle\sin (\pi+x) = -\sin x$
16. $\displaystyle\sin (2\pi-x) = -\sin x$
17. $\displaystyle\cos \left(\frac\pi2-x\right) = \sin x$
18. $\displaystyle\cos \left(\frac\pi2+x\right) = \sin x$
19. $\displaystyle\cos (\pi-x) = -\cos x$
20. $\displaystyle\cos (\pi+x) = -\cos x$
21. $\displaystyle\cos (2\pi-x) = \cos x$

- **Double Angle**

22. $\sin 2x=2\sin x\cos x$
23. $\begin{aligned}[t]\cos 2x &=2\cos^2 x - 1 \\ &= 1 - 2\sin^2 x\\ &= \cos^2 x-\sin^2 x\end{aligned}$

24. $\displaystyle\tan 2x=\frac{2\tan x}{1+\tan^2x}$

- **Triple Angle**

25. $\sin 3x=3\sin x - 4\sin^3 x$
26. $\cos 3x=4\cos^3 x - 3\cos x$

27. $\displaystyle\tan 3x=\frac{3\tan x - \tan^3 x}{1-3\tan^2 x}$

- **Sum/Difference of Sines and Cosines**

28. $\displaystyle\cos a + \cos b=2\cos \left(\frac{a+b}2\right)\cos\left(\frac{a-b}2\right)$

29. $\displaystyle\cos a - \cos b=-2\sin \left(\frac{a+b}2\right)\sin\left(\frac{a-b}2\right)$
30. $\displaystyle\sin a + \sin b=2\sin \left(\frac{a+b}2\right)\cos\left(\frac{a-b}2\right)$
31. $\displaystyle\sin a - \sin b=2\cos \left(\frac{a+b}2\right)\sin\left(\frac{a-b}2\right)$

- **Product of Sines and Cosines (Inverse of 28-31)**

32. $2\cos a\cos b = \cos (a+b)+\cos(a-b)$
33. $-2\sin a\sin b = \cos (a+b)-\cos(a-b)$
34. $2\sin a\cos b = \sin (a+b)+\sin(a-b)$

35. $2\cos a\sin b = \sin (a+b)-\sin(a-b)$

- **Zero Values\***

36. $\sin x = 0 \implies x=n\pi, n\in Z$

37. $\displaystyle\cos x = 0 \implies x=(2n+1)\frac\pi2, n\in Z$

- **Equal Values\***

38. $\sin x = \sin y \implies x = n\pi + (-1)^ny$
39. $\cos x = \cos y \implies x = 2n\pi \pm y$
40. $\tan x = \tan y \implies x = n\pi  + y$

\*These identities can be easily represented by the Unit Circle.
