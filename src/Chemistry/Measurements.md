---
title: Chemical Measurements
headertext: JEE Chemistry
author: null
subtitle: |
  \textbf{Unit 1:} Some Basic Concepts in Chemistry
...

# **Chemical Measurements**

> **Topics:** Physical quantities and their measurements in Chemistry; Precision and Accuracy; Significant Figures; SI Units; Dimensional Analysis

## Properties of Matter

All substances have various characteristic properties. These properties can be physical or chemical.

**Physical properties** can be measured/observed without changing the identity of a substance. (_Eg: Color, Mass, Melting and Boiling Point_)

On the other hand, the measurement of **Chemical properties** require the occurence of a chemical change. (_Eg: Acidity, Basicity, Combustibility_)

## Measuring Physical Properties

Physical properties such as mass, length, volume, etc. are quantitative in nature, and are expressed by a number followed by units.

$$\pu{47km}$$

## SI Units
By convention, scientists use the **SI System of Units** as a standard for measurement of various physical properties.

In the SI system, units for **seven** base quantities are defined. (See Figure 1.) All the other quantities can be derived by from the base quantities.

![Definition of SI Base units](/images/2022-06-12-22-49-50.png)

> **Derived Units**
> 
> SI Units for quantities such as speed, force, energy can be derived from the seven base units.
> $$\pu{Speed: m s-1}$$
> $$\pu{Force: kg m s-2}$$
> $$\pu{Energy: kg m2 s-2}$$

### Common prefixes

These prefixes are used with the SI units to express a large or small quantities.

|**Multiple**|**Prefix**|**Symbol**|
|:----:|:----:|:----:|
|$10^{-15}$|femto|$\pu{f}$|
|$10^{-12}$|pico|$\pu{p}$|
|$10^{-9}$|nano|$\pu{n}$|
|$10^{-6}$|micro|$\pu{\mu}$|
|$10^{-3}$|milli|$\pu{m}$|
|$10^{3}$|kilo|$\pu{k}$|
|$10^{6}$|mega|$\pu{M}$|
|$10^{9}$|giga|$\pu{G}$|
|$10^{12}$|tera|$\pu{T}$|

## Physical Properties

### Mass
In the SI system, mass is measured in $\pu{kg}$. However, in a laboratory, $\pu{g}$ is used due to small amounts of chemicals used.

> In chemistry, the terms 'weight' and 'mass' are often interchangably used.

### Volume
The SI unit of volume is $\mathbf{\pu{m3}}$. In a chemical laboratory, $\mathbf{\pu{cm3}}$ or  $\mathbf{\pu{dm3}}$ is often used.

A common unit of volume is $l$, which is used for measurement of volume of liquids.

$$\pu{1 \textit{l}~ = 1 dm3 = 1000 cm3}$$

The volumes of liquids can be measured using laboratory devices like **burette**, **pipette**, and **graduated cylinder**.

### Density
Density refers to the amount of mass of a substance per unit volume. If density is more, $\text{\underline{it means particles are more closely packed}}$.

$$\pu{Density = \frac{Mass}{Volume}}$$

$$\pu{SI unit of density\rightarrow kg m-3}$$

In a lab, density is often expressed in $\pu{g cm-3}$

### Temperature
The SI Unit of temperature is Kelvin ($\pu{K}$). However, around the world people use $\pu{^oC}$ and $\pu{^oF}$ to measure temperature.

$$\pu{^oF=\frac{9}{5}(^oC) + 32}$$
$$\pu{K=^oC + 273.15}$$

> In the Kelvin scale, the temperature $\pu{0K}$ is referred to as the $\textbf{absolute zero}$, as it is the minimum temperature possible.

|**Scale**|**Water Freezing**|**Water Boiling**|**Room Temperature**|
|:---:|:---:|:---:|:---:|
|$\pu{^oC}$|$\pu{0^oC}$|$\pu{100^oC}$|$\pu{25^oC}$|
|$\pu{^oF}$|$\pu{32^oF}$|$\pu{212^oF}$|$\pu{77^oF}$|
|$\pu{K}$|$\pu{273.15K}$|$\pu{373K}$|$\pu{298K}$|

## Scientific Notation
To express very large or very small numbers, we use $\text{\underline{scientific notation}}$.

Here, the number is expressed as a product of $N$ and $10^n$ where $N$ is a number from 1 to 10 (not including 10), and $n$ is any integer.

$$N\times 10^n\tag{$0\le N<10$; $n\in \mathbb{Z}$}$$

$$0.00016=\pu{1.6E-4}$$
$$232.508=\pu{2.32508E2}$$
$$200000=\pu{2E5}$$

> - The exponent is equal to the number of places the decimal point was shifted. 
> - If the point is shifted to the right (the number is increased), then the exponent is negative. (and vice versa) 

> **Operations on numbers in Scientific Notation** 
> 
> - **Multiplication and Division**: Numbers can be directly multiplied when in scientific notation. Here, the exponents add/subtract accordingly.
> $$(\pu{1.6E9})\times(\pu{6.9E-3})$$
> $$=1.6\times 6.9\times 10^{6}$$ 
> $$=11.04\times 10^{6}$$ 
> 
> - **Addition and Subtraction**: We need to convert both the numbers to have the same exponent in order to add or subtract them.
> $$(\pu{1.6E9})+(\pu{6.4E8})$$
> $$(\pu{16E8})+(\pu{6.4E8})$$
> $$22.4\times 10^8$$

## Rounding Off Results

Often, we will need to round off numbers to indicate the amount of precision in the answer. (In this section, all numbers are rounded off to the nearest tenths as an example.)

**Steps to round off a number**

- If the digit to be removed is more than 5, the preceding number is increased by 1.
  $$32.47\rightarrow 32.5$$

- If the digit to be removed is less than 5, the preceding number is not changed.
  $$32.43\rightarrow 32.4$$

- If the digit to be removed is 5, then:
  - the preceding number is not changed if it is even.
  - the preceding number is increased by 1 if it is odd.
  $$32.45\rightarrow 32.4$$
  $$32.75\rightarrow 32.8$$

> **Precise and Accurate Measurements**\
> $\text{\underline{Precision}}$ refers to the closeness of two results with each other. ($1.93$ and $1.95$)\
> $\text{\underline{Accuracy}}$ refers to the agreement of a result with the true value. ($1.99$ and the true value is $2.00$)

## Significant Figures

Whenever we make a measurement: say $\pu{35.45g}$, there is bound to be some error. Errors in measurement can arise due to a variety of reasons, primarily due to the capabalities of the measuring device.

For example, lets say you measure the length of an object to be $\pu{10.3cm}$ using a 30 cm ruler. It is important to note that the least count the ruler is $\pu{0.1cm} =\pu{1mm}$. Therefore, it is possible that the actual length of the object is not actually $\pu{10.3cm}$, some value close to (higher or lower than) $\pu{10.3cm}$ which cannot be accurately measured by the ruler. On measuring the object with a vernier calipers, we find that the actual length is $\pu{10.3124cm}$.

$$\text{Measurement}=\pu{10.3cm}$$
$$\text{Actual Value}=\pu{10.3124cm}$$

Here, we observe, that last digit of the measurement, $3$ uncertain. On accounting for the error in the measurement, we can write the value as $\pu{10.3\pm 0.1 cm}$, meaning the ${10}$ is certain, and the ${3}$ is uncertain.

**Significant Figures** are *meaningful digits* which include all the digits which are known with certainty, plus one digit which is estimated or uncertain. The uncertainity is indicated by the last significant digit, which is uncertain. Thus, by convention, in the measurement $\pu{11.46L}$, the uncertainity is $\pm1$ in the last digit, $6$.

### Determining Significant Figures
- All non-zero digits are significant.
  - Eg: $\pu{13.24mg}$ has 4 significant figures.
- Zeroes before the first significant digit are insignificant.
  - Eg: $\pu{0.057m}$ has 2 significant figures.
- Zeroes between two non-zero digits are significant.
  - Eg: $\pu{1.02km}$ has 3 significant figures.
- Zeroes at the end of the number are significant, if they are at the right of the decimal point.
  - Eg: $\pu{0.400g}$ has 3 significant figures.[^endfig]
- Zeroes at the end of the number maybe insignificant when there is no decimal point. Otherwise, the uncerainty is ambiguous. (To avoid ambiguity, these numbers are better represented in scientific notation.)
  - Eg: $\pu{100m}$: Here, it is not clear whether the uncertainty in measurement is 1, 10 or 100. Generally, we assume that the 00 in 100 are estimated and do not represent the actual measurement. Thus, it has only 1 significant digit.
  - Eg: $100.\text{ m}$ has 3 significant figures. The decimal point indicates that $100$ is the actual measured value.
  - Eg: $\pu{100.0m}$ has 4 significant figures.
- Counting numbers have infinite significant figures. This is because there is no error in the measurement.
  - Eg: The measurement "$30 \text{ eggs}$" has $\infty$ significant figures.
- When numbers are written in scientific notation, all digits are significant.
  - Eg: $6.022\times 10^{23}$ has 4 significant figures.
  - Eg: $2.40\times 10^{-5}$ has 3 significant figures.

[^endfig]: Here, $\pu{4.00g}$ is different from $\pu{4g}$, because the two extra zeroes indicate that the measurement is more precise, i.e. $4\pm 0.01$ rather than $4\pm 1$. Thus, it has more significant figures.

### Operations of Significant Figures

**Addition and Subtraction** \
The result cannot have $\text{\underline{more digits after the decimal point}}$, than the original numbers.

$$\begin{aligned}12.11+18.0+1.012 &=31.122 \\&=31.1\end{aligned}$$

Here, since $18.0$ only has one decimal place, the result should be reported with only one digit after the decimal point.

**Multiplication and Division** \
The result cannot have $\text{\underline{more significant figures}}$, than the original numbers.

$$\begin{aligned}12.64\times 0.12 &= 1.5168 \\&=1.5\end{aligned}$$

Here, since $0.12$ only has two significant figures, the result should be reported with only two significant figures.

## Dimensional Analysis

**Dimensional Analysis** or the **Unit Factor Method** is a method to convert measurements into different units.

Eg: Convert $\pu{2L}$ to $\pu{m3}$.

\begin{align*}
1~\mathrm{L} &= 100~\mathrm{cm^3} \\
\implies 1 &= \frac{1000~\mathrm{cm^3}}{1~\mathrm{L}} \\
1~\mathrm{m^3} &= 10^6~\mathrm{cm^3} \\
\implies 1 &= \frac{1~\mathrm{m^3}}{10^6~\mathrm{cm^3}}
\end{align*}

\begin{align*}
2~\mathrm{L} &= 2~\mathrm{L}\times \frac{1000~\mathrm{cm^3}}{1~\mathrm{L}} \times \frac{1~\mathrm{m^3}}{10^6~\mathrm{cm^3}}\\
2~\mathrm{L} &= 2\times 10^{-3}~\mathrm{m^3}
\end{align*}

Here, fractions such as $\frac{1000~\mathrm{cm^3}}{1~\mathrm{L}}$ are known as unit factors, since they are equal to 1. These can be multiplied to a measurement without changing its value.

*****

## Questions

1. How many significant figures will be present in the result of this calculation?
     $$\frac{2.5\times 1.25\times 3.5}{2.01}$$

2. What is the difference between expressing the weight of a solid as $\pu{36.5E3g}$ and $\pu{36.50E3g}$?

3. A student performs a titration with different burettes and finds titre values of $\pu{25.2 mL}$, $\pu{25.25 mL}$, and $\pu{25.0 mL}$.
The number of significant figures in the average titre value is ________. **[IIT-JEE 2010]**

4. A measured temperature on Fahrenheit scale is $\pu{200^oF}$. What will this reading be on celsius scale?

5. In which of the following numbers all zeros are significant?

    (A) 0.500 
    (A) 30.000 
    (A) 0.00030
    (A) 0.0050
