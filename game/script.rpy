

image attic = im.Scale("atico.png", config.screen_width, config.screen_height)
image bedroom =im.Scale("bedroom.png", config.screen_width, config.screen_height)
image garden = im.Scale("garden.png", config.screen_width, config.screen_height)
image school = im.Scale("school.png", config.screen_width, config.screen_height)
image city_night = im.Scale("city_nigth.png", config.screen_width, config.screen_height)
image rainy_street = im.Scale("rainy_street.png", config.screen_width, config.screen_height)
image city_restored = im.Scale("city_restored.png", config.screen_width, config.screen_height) 
image depresion = im.Scale("depresion.png", config.screen_width, config.screen_height)
image duo_imparable = im.Scale("duo_imparable.png", config.screen_width, config.screen_height)
image caos_1 = im.Scale("caos_1.png", config.screen_width, config.screen_height)
image hana normal = "hana.png"
image lumen normal = "lumen.png"
image akira normal = "akira.png"
image carta_viento = "carta_viento.png"
image carta_espejo = "carta_espejo.png"


define responsabilidad_pts = 0
define amistad_pts = 0
define secreto_revelado = False


define h = Character("Hana", color="#ffc0cb")     # Protagonista
define l = Character("Lumen", color="#00ffff")    # Guardián
define a = Character("Akira", color="#c8c8ff")    # Amigo

# Cartas Mágicas
define cv = Character("Carta del Viento", color="#5dff5d")
define ce = Character("Carta del Espejo", color="#c8c8c8")




label start:
    scene attic with fade 
    
    "Hace una semana, Hana encontró un libro polvoriento en el ático."
    "Al abrirlo, un destello liberó varias cartas encantadas."

    show lumen normal at right 

    l "¡Oh, genial! ¡Ahora estamos en un lío de tamaño cósmico!"
    hide lumen normal
    show hana normal at left
    h "¡Lumen! Ya te dije que lo siento. ¿Cómo se supone que voy a atraparlos a todos?"
    hide hana normal
    show lumen normal at right 
    l "Tienes el libro, niña. ¡Tienes el poder!"

 
    menu primer_deber:
        "¿Qué hacer con el libro?"
        "Seguir recolectando las cartas (Aceptar el deber).":
            jump decision_akira
        "Abandonar el libro y buscar vivir normalmente.":
            jump rama_3_rebeldia


# -----------------------------------------------------------------------------
# 3. DECISIÓN CLAVE 1 (DC1): CONTAR O NO A AKIRA (Define Rama 1 o Rama 2)
# -----------------------------------------------------------------------------

label decision_akira:
    scene bedroom with fade

    hide lumen 
    show akira normal at right
    
    a "Te veo rara últimamente, Hana. ¿Todo bien?"
    
    # DECISIÓN CLAVE 1
    menu contar_akira:
        "¿Contar a Akira el secreto?"
        
        "Mantener el secreto y aceptar el deber sola. ":
            a "Está bien, supongo. Si necesitas algo, dímelo."
            hide akira normal
            jump rama_1_responsabilidad
        
        "Compartir el secreto con Akira e involucrarlo.":
            $ secreto_revelado = True
            a "¡¿Cartas mágicas?! ¿En serio? Suena... imposible. Pero te creo."
            $ amistad_pts += 1
            jump rama_2_amistad


# -----------------------------------------------------------------------------
# 4. RAMA 1: EL CAMINO DE LA RESPONSABILIDAD (Solitaria)
# -----------------------------------------------------------------------------

label rama_1_responsabilidad:
    scene city_night with fade 
    
    show hana normal at left    
    h "Tengo que hacer esto sola. Es mi responsabilidad."
    hide hana normal
    show lumen normal at right
    l "Como quieras, señorita 'Lo Haré Sola'."
    hide lumen normal
    show carta_viento at right
    cv "¡Soy libre! ¡A volar sombreros!"
    hide carta_viento
    show hana normal at left    
    h "¡Vuelve aquí, Carta del Viento!"
    hide hana normal

    # DECISIÓN CLAVE 2 (DC2): ¿Enfrentar sola o pedir ayuda a Lumen?
    menu primer_enfrentamiento_solo:
        "DECISIÓN CLAVE 2: ¿Cómo enfrentar a la Carta del Viento?"

        "Enfrentar sola y con disciplina.":
            $ responsabilidad_pts += 1
            show hana normal at left    
            h "¡Control! ¡Debo concentrarme!"
            hide hana normal
            "Hana se concentra. Después de un gran esfuerzo, logra sellar la carta."
            jump punto_reunion_solo

        "Pedir ayuda a Lumen.":
            $ amistad_pts += 1
            show lumen normal at right
            l "¡Déjame esto a mí! Concéntrate, pero sígueme."
            hide lumen normal
            "Con la guía de Lumen, Hana logra sellar la carta. Fue más fácil, pero dependió de él."
            jump punto_reunion_solo
            
label punto_reunion_solo:
    "La recolección de cartas continúa. Es difícil, pero Hana es metódica."
    show carta_espejo at right
    "Finalmente, solo queda la Carta del Espejo, la más compleja."
    hide carta_espejo
    
  
    if responsabilidad_pts >= 1:
        jump final_1A
    else:
        jump final_1B


# -----------------------------------------------------------------------------
# 5. RAMA 2: EL CAMINO DE LA AMISTAD (Compartida con Akira)
# -----------------------------------------------------------------------------

label rama_2_amistad:
    scene city_night with fade
    
    show akira normal at center

    a "Muy bien, Hana. ¿Cuál es el plan? Hay que ser lógicos."
    hide akira normal
    show lumen normal at right
    l "Ugh, el 'racionalista' al rescate."
    hide lumen normal

    show carta_viento
    cv "¡Jijiji! ¿Dos contra mí? ¡Qué divertido!"
    hide carta_viento

    # DECISIÓN CLAVE 2 (DC2): ¿Enfrentar sola o con ayuda?
    menu primer_enfrentamiento_duo:
        "DECISIÓN CLAVE 2: ¿Cómo enfrentar a la Carta del Viento?"
        "Enfrentar sola (Hana) con el apoyo de Akira.":
            $ responsabilidad_pts 
            show akira normal at center
            a "Yo distraeré a la carta con esto. ¡Tú ataca, Hana!"
            hide akira normal
            "Trabajando en equipo, Hana sella la carta. El lazo de confianza se fortalece."
            jump punto_reunion_duo

        "Pedir ayuda a Lumen y Akira observa.":
            show lumen normal at right
            $ amistad_pts += 1
            l "¡Ahora, Akira! ¡Lánzale el extintor mágico!"
            hide lumen normal
            show akira normal at left
            a "¡Entendido!"
            hide akira normal
            "Lumen y Akira logran acorralar la carta, Hana la sella. Akira se pregunta si solo es un asistente."
            jump punto_reunion_duo

label punto_reunion_duo:
    "La misión avanza, el dúo Hana-Akira recolecta varias cartas."

  
    show akira normal at left
    a "Hana, el poder de las cartas es increíble. ¿Por qué sellarlas por completo?"
    hide akira normal

    if amistad_pts >= 2:
        # Final 2A: Dúo Imparable (Amistad total)
        show hana normal at right
        h "Es nuestro deber, Akira. Pero podemos usarlas con cuidado. Juntos."
        hide hana normal
        show akira normal at left
        a "Tienes razón. Un poder compartido es un poder controlado."
        hide akira normal
        jump final_2A
    else:
        # Final 2B: Traición (Amistad parcial / Akira se sintió excluido)
        show hana normal at right
        h "No, Akira. Esto no es un juego. Deben sellarse."
        hide hana normal
        show akira normal at left
        a "Lo siento, Hana. Yo puedo hacerlo mejor. El poder no debe desperdiciarse."
        hide akira normal
        "Akira, cegado por la ambición, roba las cartas restantes y desaparece. Hana queda con el corazón roto y la misión inconclusa."
        jump final_2B


# -----------------------------------------------------------------------------
# 6. RAMA 3: EL CAMINO DE LA REBELDÍA (Ignorar el deber)
# -----------------------------------------------------------------------------

label rama_3_rebeldia:
    scene school with fade 
 
    show hana normal at left
    hide lumen 
    
    $ secreto_revelado = False
    show hana normal at left
    h "No quiero esta carga. Lo voy a ignorar y a vivir mi vida."
    hide hana normal
  
    show lumen normal at right
    l "¡No puedes! ¡El caos se desatará!"
    hide lumen normal
    show hana normal at left
    h "Que se desate. No es mi problema."

    hide hana normal

    scene caos_1 with fade
    "Hana intenta volver a su vida normal. Pero la ciudad comienza a sufrir extraños sucesos."
    
    show carta_viento at right

    cv "¡Jajaja! ¡Tornados de palomitas!"
    hide carta_viento

    show carta_espejo at right
    ce "¡Reflejando los peores miedos de la gente!"
    hide carta_espejo
   
    show lumen normal at right 
    l "¡Hana, es tu última oportunidad! ¡El caos es total! ¡Mira la ciudad!"
    hide lumen normal
    hide hana normal
    menu enfrentar_o_huir:
        "¿Qué hacer ante el caos total?"
        
        "Usar el dolor de la culpa para despertar un poder interno.":
            show hana normal at left 
            h "¡No lo haré por el libro, lo haré por mi ciudad!"
            hide hana normal       
            "Impulsada por la desesperación, Hana despierta un poder latente, una magia propia."
            jump final_3A
            
        "Huir y culparse por no haber actuado antes.":
            show hana normal
            h "Soy una cobarde... Debí haber actuado..."
            hide hana normal
            "El caos persiste. Las cartas se pierden para siempre. Hana vive con el peso de la culpa."
            jump final_3B


# -----------------------------------------------------------------------------
# 7. FINALES (Asegúrate de que el fondo final es visualmente apropiado)
# -----------------------------------------------------------------------------

label final_1A:
    hide all
    scene garden with fade
    show hana normal at center
    h "El deber es pesado, pero la ciudad está a salvo. A partir de hoy, soy la Guardiana Oficial."
    hide hana normal
    show lumen normal
    l "Y yo, tu asistente muy molesto y muy bien pagado."
    
    "El mundo mágico y el mundo real tienen una nueva Protectora."
    hide lumen normal
    "FIN DEL JUEGO:  GUARDIA OFICIAL"
    return

label final_1B:
    hide all
    scene depresion with fade
    "La presión de la responsabilidad era demasiado para Hana."

    h "Solo quiero que esto termine. Quiero volver a mis clases y a mis amigos."
    
    "Lumen, por el bien de Hana, selló el libro, borrando la memoria del mundo mágico de la mente de la chica."
    "Hana regresó a la escuela, pero la sensación de haber perdido algo vital nunca la abandonó."
    "FIN DEL JUEGO: - CONSUMIDA POR LA PRESIÓN"
    return

label final_2A:
    hide all
    scene duo_imparable with fade
    h "Otro sellado exitoso. Somos un gran equipo, Akira."
    a "Dos cerebros son siempre mejor que uno, Hana. Y la próxima vez, ¡usa tu poder en lugar de la disciplina!"
    
    "Juntos, Hana y Akira forman una alianza mágica inquebrantable, lidiando con las amenazas con estrategia y confianza mutua."
    "FIN DEL JUEGO:  - EL DÚO IMPARABLE"
    return

label final_2B:
    hide all
    scene rainy_street with fade
    h "Akira... ¿por qué? ¿Por qué me traicionaste?"
    
    "Bajo la lluvia, Hana siente el dolor de la traición. Akira, cegado por la ambición de un poder que sintió que Hana no valoraba, huyó con el libro."
    "La magia se desequilibra sin el libro y la confianza se rompe. La misión de Hana ahora es recuperar no solo las cartas, sino a su amigo."
    
    "FIN DEL JUEGO:- LA AMBICIÓN ROMPE LA CONFIANZA"
    return

label final_3A:
    hide all
    scene city_restored with fade

    h "No necesito el libro para proteger lo que es mío. Mi poder viene de aquí, de mi voluntad."
    
    "El poder latente de Hana despierta, restaurando el orden en la ciudad sin depender de Lumen o el antiguo libro."
    "Ella se convierte en una Guardiana, no por deber, sino por elección propia. Un nuevo capítulo de la magia comienza, libre de reglas ancestrales."
    "FIN DEL JUEGO:- PODER ALTERNATIVO"
    return

label final_3B:
    hide all
    scene depresion with fade
    "La ciudad sigue sumida en el caos. Hana se sienta sola, la oscuridad del cuarto reflejando la oscuridad de su culpa."
    
    h "Debí haberlo hecho... Por mi culpa, la gente... No hay vuelta atrás."
    
    "El libro y las cartas se pierden en el mundo. El caos se normaliza en un estado de temor constante. Hana vive el resto de su vida con el peso de la oportunidad perdida."
    
    "FIN DEL JUEGO: FINAL 3B - ATRAPADA EN LA CULPA"
    return