import os
import torch

from initno.pipelines.pipeline_sd_initno import StableDiffusionInitNOPipeline
from diffusers import EulerAncestralDiscreteScheduler


# ---------
# Arguments
# ---------
SEEDS           = [0]
SD14_VERSION    = "CompVis/stable-diffusion-v1-4"
SD15_VERSION    = "runwayml/stable-diffusion-v1-5"
SD_TURBO        = "stabilityai/sd-turbo"
PROMPT          = "a cat and a rabbit"
token_indices   = [2, 5]
result_root     = "results"

os.makedirs('{:s}'.format(result_root), exist_ok=True)

def main():

    pipe = StableDiffusionInitNOPipeline.from_pretrained(SD_TURBO).to("cuda")
    # print(list(pipe.unet.attn_processors.keys())[:10])
    # pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(
    #     pipe.scheduler.config, timestep_spacing="trailing")
    # after loading the pipe
    # n_text_tokens = pipe.tokenizer(PROMPT, return_tensors="pt").input_ids.shape[-1]  # 128 for Turbo
    # pipe.attention_store.attn_res = (1, n_text_tokens)   # now 1×128  → product = 128


    # use get_indices function to find out indices of the tokens you want to alter
    pipe.get_indices(PROMPT)
    # print("Token Indices:", indices)

    for SEED in SEEDS:

        print('Seed ({}) Processing the ({}) prompt'.format(SEED, PROMPT))

        generator = torch.Generator("cuda").manual_seed(SEED)
        images = pipe(
            prompt=PROMPT,
            token_indices=token_indices,
            guidance_scale=0.0,
            generator=generator,
            num_inference_steps=3,
            max_iter_to_alter=3,
            result_root=result_root,
            seed=SEED,
            run_sd=False,
        ).images

        image = images[0]
        image.save(f"./{result_root}/{PROMPT}_{SEED}.jpg")


if __name__ == '__main__':
    main()