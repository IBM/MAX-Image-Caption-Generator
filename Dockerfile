FROM codait/max-base

ARG model_bucket=http://max-assets.s3-api.us-geo.objectstorage.softlayer.net/tf/im2txt
ARG model_file=im2txt_ckpt.tar.gz

WORKDIR /workspace

RUN wget -nv ${model_bucket}/${model_file} --output-document=/workspace/assets/${model_file}
RUN tar -x -C assets/ -f assets/${model_file} -v

RUN pip install tensorflow && \
    pip install Pillow

COPY . /workspace

EXPOSE 5000

CMD python app.py