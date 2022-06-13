---
headertext: 11th Mathematics (JEE)
...

# **Complex Numbers**

In the **real** number system, the solution for $\gdef\Re{\mathrm{Re}\ }\gdef\Im{\mathrm{Im}\ }x^2=-1$ is undefined. This is because of the fact that the square of any real number is always non-negative.

In order to solve such equations, we extend the real number system to the **Complex Numbers**.

$$
\boxed{
    \begin{aligned}
    \sqrt{-1}=i\\
i^2=-1\end{aligned}}
$$

We define a value $i$ to be the square root of -1.

> Here, $i$ is called a _imaginary number_, since it is not present in the real numbers.

## Complex Numbers

A Complex Number is a number which has both a real and imaginary component.

$$z = a+ib \tag{$a\in R, b\in R$}$$

$$\Re z=a$$
$$\Im z=b$$

Examples: $\displaystyle 2+5i,\quad 6+i\sqrt3,\quad -\frac1{11}+i\frac2{11}$

> **Equality** 
> $$z_1=a+ib$$ 
> $$z_2=c+id$$ 
> $$\text{if }a=c\text{ and }b=d, \implies z_1=z_2$$

## Square Root of a Negative Number

$$\sqrt{-1}= i$$
$$\sqrt{-5}= i\sqrt{5}$$
$$\sqrt{-16}= 4i$$
$$\sqrt{-a}= i\sqrt a$$

## Powers of i

$$
\begin{aligned}
i^1 &=i  &&= i^{4k}\\
i^2 &=-1 &&= i^{4k+1}\\
i^3 &=-i &&= i^{4k+2}\\
i^4 &=1  &&= i^{4k+3}
\end{aligned}
$$

## Operations

### Addition and Subtraction

$$z_1=a+ib$$
$$z_2=c+id$$
$$z_1+z_2=(a+c)+i(b+d)$$

### Multiplication

$$z_1=a+ib$$
$$z_2=c+id$$

$$
\begin{aligned}
z_1z_2&=(a+ib)(c+id)\\
&= ac+adi+bci+bdi^2\\
&= (ac-bd)+i(ad+bc)
\end{aligned}
$$

### Modulus

Modulus of a complex number is defined as the square root of the sum of the squares of the real and imaginary components.

$$z=a+ib$$
$$|z|=\sqrt{a^2+b^2}$$

### Conjugate

The conjugate of a complex number is derived by inverting the sign of the imaginary component.

$$z=a+ib$$
$$\overline z=a-ib$$

> **Example** 
>
> $$|-3+4i|=\sqrt{(-3)^2+4^2}=5$$ 
> 
> $$\overline{-3+4i}=-3-4i$$

### Inverse (Reciprocal)

For any complex number $z$, its inverse is defined as:
$$\frac1z=z^{-1}=\frac{\overline z}{|z|^2}$$

> **Example** 
> 
> $$\begin{aligned}\frac1{-3+4i}&=\frac{\overline{-3+4i}}{(-3)^2+4^2}=\frac{-3-4i}{25}\\&=\frac{-3}{25}-i\frac{4}{25}\end{aligned}$$

### Division

$$z_1=a+ib$$
$$z_2=c+id$$
$$\frac{z_1}{z_2}=z_1\times \frac1{z_2}$$

> **Modulus and Conjugate Properties**
>
> - $|z_1z_2|=|z_1||z_2|$
> - $\overline{z_1z_2}=\overline{z_1}\ \overline{z_2}$
>
> - $\displaystyle\left|\frac{z_1}{z_2}\right|=\frac{|z_1|}{|z_2|}$
> - $\displaystyle\overline{\left(\frac{z_1}{z_2}\right)}=\frac{\overline{z_1}}{\overline{z_2}}$
> - $\overline{z_1\pm z_2}=\overline{z_1}\pm \overline{z_2}$

## Visual Representation

We know that all real numbers can be visually represented using the **real number line**.

![](/images/2022-05-31-01-38-22.png){ width=650px }

All real numbers ($2, -7/5, \sqrt 3, \pi,$ etc.) are distinct points on this number line.

When we extend the number system to include imaginary numbers ($i$), we need to add another dimension to represent _all complex numbers._

The **Complex Number Plane** is the visual representation of the set of all Complex Numbers, where the x-axis represents _real numbers_ and the y-axis represents _imaginary numbers_

![The Complex Number Plane](/images/2022-05-31-01-34-44.png){ width=450px }

Each point on this plane represents a specific complex number.

Conversely, all complex numbers ($3+i, \frac{-3}{2}+i\sqrt2, 57,$ etc.) are represented by a point on the plane.

> For any complex number, the modulus and conjugate can be visualised on the complex plane.
>
> ![](/images/2022-05-31-15-27-09.png)
> The modulus of the number is the distance of the point from the origin $0$.
> The conjugate of the number is the mirror image of the number on the Real axis.

## Cartesian and Polar Coordinates

In the **Cartesian Coordinate System**, we use two numbers - the x-coordinate and y-coordinate to locate a point on the plane.

![Cartesian and Polar Coordinates](/images/2022-05-31-17-15-48.png){ width=350px }

Another system of Coordinates is the **Polar Coordinate System**. Here, the two numbers used to represent a point in a plane are:

$$\text{Polar Coordinates: } (r,\theta)$$
$$r=\text{distance from origin}$$
$$\theta=\text{angle with horizontal axis}$$

> For example, the point $P(5, \pi/3)$ represents a point which is 5 units away from the origin, making a $60\degree$ angle with the x-axis.

### Complex Numbers in Polar Form

When we represent complex numbers, we use the cartesian form $(x, y)$ where $x=\Re z$ and $y=\Im z$. We can also use the polar system to do so.

Let $z$ be a complex number.

![](/images/2022-05-31-19-12-30.png)

Here, we can calculate the x and y coordinates using **trigonometry**.

$$x=r\cdot\cos\theta$$
$$y=r\cdot\sin\theta$$

$$z=r\cos\theta+ir\sin\theta$$
$$\boxed{z=r(\cos\theta+i\sin\theta)}$$
$$\ \tag{$r=\sqrt{x^2+y^2}=|z|$}$$

This is known as the Polar Representation of a Complex Number.

Here, $\theta$ is known as the **argument** of $z$.

> There will be multiple values of $\theta$ which satisfy the sin and cos. By convention, we use the value $-\pi<\theta\le\pi$

> **Example**
> Find modulus and argument of $1-i$. Also convert it to the polar form.
>
> $$z=1-i$$
> $$r=|z|=\sqrt{1^2+(-1)^2}$$ 
> $$\boxed{r=\sqrt2}$$ 
> $$\cos\theta=\frac{\Re z}r=\frac1r=\frac1{\sqrt2}$$ 
> $$\sin\theta=\frac{\Im z}r=\frac{-1}r=\frac{-1}{\sqrt2}$$
> sin is $-$ve and cos is +ve $\implies$ Angle in Quadrant IV
> $$\boxed{\theta = \frac{-\pi}{4}}$$
> Polar Form:
> $$\boxed{z=\sqrt2\left(\cos\frac{-\pi}4+i\sin\frac{-\pi}4\right)}$$
