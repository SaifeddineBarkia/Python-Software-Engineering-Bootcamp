FROM python:3.9-alpine as base

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

COPY requirements.txt ./
RUN PIP_USER=1 pip install -r requirements.txt

# RUN if [ "$ENVIRONMENT" = "test" ] ; then PIP_USER=1 pipenv install --system --deploy --ignore-pipfile --dev ; \
#  else PIP_USER=1 pipenv install --system --deploy --ignore-pipfile; fi

FROM python:3.9-alpine

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
COPY --chown=user:myapp --from=base ${PYROOT}/ ${PYROOT}/

RUN  mkdir -p /usr/src/workspace/app
WORKDIR  /usr/src/workspace

COPY  --chown=user:myapp app ./app

USER user

CMD ["uvicorn","app.main:appi","--host","0.0.0.0","--port","8080"]
# CMD ls -l ./app
