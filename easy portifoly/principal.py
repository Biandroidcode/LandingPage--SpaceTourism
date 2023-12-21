import pygame
import constantes
import sprites
class Game:
    def__init__(self)
    #criando a tela do jogo
    pygame.init()
    pygame.mixer.unit()
    self.tela= pygame.display.set_mode((constantes.LARGURA.constantes.ALTURA))
    pygame.display.set_caption(constantes.TITULO_JOGO)
    self.relogio=pygame.time.Clock()
    self.esta_rodando=True
     
    def novo_jogo(self):
     	self.todas_as_sprites=pygame.sprites.group()
     	self.rodar()
     
     def eventos(self):pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT;
                if self.jogando;
                self.jogando= False
                self.esta_rodando= False
                def atualizar_sprites(self):
                    self.todas_as_sprites.update()

                    def desenhar_sprites(self)
                    self.tela.fill(constantes.PRETO)
                    self_todas_as_sprites.draw(self.tela)
                    pygame.display.flip()
        def mostrar_tela_start(self):
            pass
        def mostrar_tela_game_over(self)
        pass
        g=Game()
        g=mostrar_mostrar_tela_start()

        while g.esta_rodando:
           g.novo_jogo()
           g.mostrar_tela_game_over()
    
