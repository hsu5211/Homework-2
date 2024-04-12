# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Path : tokenB -> tokenA -> tokenC -> tokenE -> tokenD -> tokenC -> tokenB
> Final reward = 22.592156
> |  tokenIn  | tokenOut | amountIn | amountOut |
> |:---------:|:--------:|:--------:|:---------:|
> |     B     |     A    | 5.000000 |  5.666667 |
> |     A     |     C    | 5.666667 |  2.380000 |
> |     C     |     E    | 2.380000 |  1.537964 |
> |     E     |     D    | 1.537964 |  3.477202 |
> |     D     |     C    | 3.477202 |  6.739982 |
> |     C     |     B    | 6.739982 | 22.592156 |

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Slippage is when the quoted price of an asset changes when a trade is executed, resulting in a trader receiving less/more tokens as a result. Uniswap V2 addresses the issue of slippage by allowing users to set a maximum slippage tolerance when they initiate a trade. The trade will only be executed if the actual price falls within the user's specified slippage tolerance. Consider there two tokens in the pool, $A$ and $B$ with amount $x$ and amount $y$ respectively. According to the constant product formula $x \times y=k$, if a user wants to swap an amount $\Delta A$ of A token, the user will receives $\Delta B=y-\frac{k}{x+\Delta A}$. It shows that larger $\Delta A$ leads to more significant deviation from the expected price.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> It's a prevention from "inflation attack" by burning first MINIMUM_LIQUIDITY tokens to ensure that no one owns the entire supply of LP tokens and can easily manipulate the price.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> The formula is intended to maintain the correct ratio of assets in the pool and to ensure that the value of existing liquidity tokens is not diluted.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Attackers rapidly execute large transactions just before and after a trader submits their trade, resulting in the trader getting an unfavorable price (buying high/selling low), thereby causing a loss of the trader's assets.
