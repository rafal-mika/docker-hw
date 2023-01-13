FROM python:3
COPY . /app
WORKDIR /app


ARG RUN_TESTS=true
ARG TEST_FAILED_MSG="TESTS FAILED - BUILDING IMAGE IS STOPPED..."
RUN if [ "$RUN_TESTS" = true ]; \
    then pip install pytest && pytest main_test.py || (echo ${TEST_FAILED_MSG} && exit 1);  fi

ENTRYPOINT ["python"]
CMD ["main.py"]
