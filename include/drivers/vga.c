/* src/drivers/vga.c */
#include "../../include/drivers.h"

#define VIDEO_MEMORY 0xB8000
#define SCREEN_WIDTH 80
#define SCREEN_HEIGHT 25
#define WHITE_ON_BLACK 0x0F

void vga_init(void) __asm__("_vga_init");
void vga_clear(void) __asm__("_vga_clear");
void vga_putc(char c) __asm__("_vga_putc");

static int cursor_pos = 0;

static void vga_scroll(void) {
    volatile char *video = (volatile char*) VIDEO_MEMORY;
    
    // Desplazar las líneas hacia arriba (1 fila menos)
    int bytes_per_line = SCREEN_WIDTH * 2;
    int total_bytes = SCREEN_WIDTH * (SCREEN_HEIGHT - 1) * 2;
    
    for (int i = 0; i < total_bytes; i++) {
        video[i] = video[i + bytes_per_line];
    }

    // Limpiar la última línea
    for (int i = total_bytes; i < SCREEN_WIDTH * SCREEN_HEIGHT * 2; i += 2) {
        video[i] = ' ';
        video[i + 1] = WHITE_ON_BLACK;
    }

    cursor_pos = SCREEN_WIDTH * (SCREEN_HEIGHT - 1);
}

void vga_init(void) {
    vga_clear();
}

void vga_clear(void) {
    volatile char *video = (volatile char*) VIDEO_MEMORY;
    for (int i = 0; i < SCREEN_WIDTH * SCREEN_HEIGHT * 2; i += 2) {
        video[i] = ' ';
        video[i + 1] = WHITE_ON_BLACK;
    }
    cursor_pos = 0;
}

void vga_putc(char c) {
    volatile char *video = (volatile char*) VIDEO_MEMORY;

    if (c == '\n') {
        cursor_pos += SCREEN_WIDTH - (cursor_pos % SCREEN_WIDTH);
    } else if (c == '\r') {
        cursor_pos -= (cursor_pos % SCREEN_WIDTH);
    } else if (c == '\t') {
        cursor_pos = (cursor_pos + 4) & ~3; // Tabulación alineada a 4 espacios
    } else if (c >= ' ') {
        video[cursor_pos * 2] = c;
        video[cursor_pos * 2 + 1] = WHITE_ON_BLACK;
        cursor_pos++;
    }

    // Si el cursor alcanza o supera el límite de pantalla, realizar scroll
    if (cursor_pos >= SCREEN_WIDTH * SCREEN_HEIGHT) {
        vga_scroll();
    }
}
