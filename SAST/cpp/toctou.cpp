#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

void create_file_securely(const char *file) {
  int fd = open(file, O_CREAT | O_EXCL | O_WRONLY, S_IRUSR | S_IWUSR);
  if (fd == -1) {
    /* Handle error */
    return;
  }

  /* Write data to the file */

  if (close(fd) == -1) {
    /* Handle error */
  }
}