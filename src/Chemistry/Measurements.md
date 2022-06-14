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
> - Multiplication and Division \
>   Numbers can be directly multiplied when in scientific notation. Here, the exponents add/subtract accordingly.
> $$(\pu{1.6E9})\times(\pu{6.9E-3})$$
> $$=1.6\times 6.9\times 10^{6}$$ 
> $$=11.04\times 10^{6}$$ 
> 
> - Addition and Subtraction \
>   We need to convert both the numbers to have the same exponent in order to add or subtract them.
> $$(\pu{1.6E9})+(\pu{6.4E8})$$
> $$(\pu{16E8})+(\pu{6.4E8})$$
> $$(16+6.4)\times 10^8$$
> $$22.4\times 10^8$$

## Rounding Off Results

Often, we will need to round off numbers to indicate the amount of precision in the answer. (In this section, all numbers are rounded off to the nearest tenths as an example.)

**Steps to round off a number** \
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
> $\underline{\text{Precision}}$ refers to the closeness of two results with each other. ($1.93$ and $1.95$)\
> $\underline{\text{Accuracy}}$ refers to the agreement of a result with the true value. ($1.99$ and the true value is $2.00$)

## Significant Digits
In any number, the significant digits are **digits with meaningful certainity, plus one.**

