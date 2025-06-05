void f(char *password, size_t bufferSize) {
  char localToken[256] = {0};
  init(localToken, password);

  // Securely clear the password buffer
  secure_clear(password, bufferSize);
  free(password);

  // Securely clear the localToken buffer
  secure_clear(localToken, sizeof(localToken));
}

void secure_clear(void *ptr, size_t len) {
  volatile unsigned char *p = (volatile unsigned char *)ptr;
  while (len--) {
    *p++ = 0;
  }
}