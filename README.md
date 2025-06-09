# InitNoTurbo

Due to the few inference steps in Stable Diffusion Turbo in comparison with Stable Diffusion 1.4, which is used in [InitNo](https://github.com/xiefan-guo/initno), and the use of lower guidance scale in SD-Turbo, the attention maps in the initial timesteps are mostly flat when using turbo model. This makes InitNo unable to optimize the initial noise. In this Repository, I have tried to adapt InitNo to be able to optimize SD-Turbo image generation with slight changes in logic.
