pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
huggingface-cli download BAAI/bge-m3 --local-dir bge-m3

#scp -r <lanta-user>@transfer.lanta.nstda.or.th:/project/lt900048-ai24tn/models/BAAI/bge-m3 .