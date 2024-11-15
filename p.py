import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Lấy kích thước màn hình
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Thiết lập màn hình với chế độ toàn màn hình
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Thêm pygame.FULLSCREEN

# Tải ảnh
image = pygame.image.load("a.png")
image = pygame.transform.scale(image, (screen_width, screen_height))  # Thay đổi kích thước ảnh để lấp đầy màn hình

# Vô hiệu hóa toàn bộ bàn phím bằng cách không xử lý các sự kiện phím
pygame.key.set_repeat(0)  # Tắt chế độ lặp phím

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        # Chặn sự kiện đóng cửa sổ
        if event.type == pygame.QUIT:
            continue  # Bỏ qua sự kiện thoát

        # Chặn mọi sự kiện phím nhấn và phím thả
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            continue  # Bỏ qua tất cả các phím nhấn và phím thả

    # Vẽ ảnh lên màn hình
    screen.blit(image, (0, 0))

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát khi vòng lặp kết thúc
pygame.quit()
sys.exit()
