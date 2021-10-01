#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *html = fopen("index.html", "w");
    FILE *tractatus = fopen("tractatus.txt", "r");

    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fprintf(html, "<html>\n");
    fprintf(html, "<head>\n");
    fprintf(html, "<title>hello world</title>\n");
    fprintf(html, "<p>why hello there</p>\n");

    while (read = getline(&line, &len, tractatus) != -1)
    {
        printf("%s", line);
    }

    fprintf(html, "</head>\n");
    fprintf(html, "</html>\n");

    fclose(html);
    fclose(tractatus);

    return 0;
}
