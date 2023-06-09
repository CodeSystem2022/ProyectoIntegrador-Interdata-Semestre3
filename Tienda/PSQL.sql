PGDMP         	                {            TiendaInterdata    15.3    15.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16547    TiendaInterdata    DATABASE     �   CREATE DATABASE "TiendaInterdata" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Argentina.1252';
 !   DROP DATABASE "TiendaInterdata";
                postgres    false            �            1259    16639    carrito    TABLE     �   CREATE TABLE public.carrito (
    nombre character varying,
    cantidad integer,
    precio integer,
    numero integer NOT NULL
);
    DROP TABLE public.carrito;
       public         heap    postgres    false            �            1259    16644    carrito_numero_seq    SEQUENCE     �   CREATE SEQUENCE public.carrito_numero_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.carrito_numero_seq;
       public          postgres    false    218                       0    0    carrito_numero_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.carrito_numero_seq OWNED BY public.carrito.numero;
          public          postgres    false    219            �            1259    16611    pagos    TABLE     �   CREATE TABLE public.pagos (
    "transacción N°" integer NOT NULL,
    monto numeric(10,2) NOT NULL,
    fecha timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    metodo character varying
);
    DROP TABLE public.pagos;
       public         heap    postgres    false            �            1259    16610    pagos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pagos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.pagos_id_seq;
       public          postgres    false    216                       0    0    pagos_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.pagos_id_seq OWNED BY public.pagos."transacción N°";
          public          postgres    false    215            �            1259    16596 	   productos    TABLE     m   CREATE TABLE public.productos (
    name character varying,
    type character varying,
    price integer
);
    DROP TABLE public.productos;
       public         heap    postgres    false            �            1259    16629    usuarios    TABLE     ]   CREATE TABLE public.usuarios (
    usuario character varying,
    clave character varying
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            t           2604    16645    carrito numero    DEFAULT     p   ALTER TABLE ONLY public.carrito ALTER COLUMN numero SET DEFAULT nextval('public.carrito_numero_seq'::regclass);
 =   ALTER TABLE public.carrito ALTER COLUMN numero DROP DEFAULT;
       public          postgres    false    219    218            r           2604    16614    pagos transacción N°    DEFAULT     t   ALTER TABLE ONLY public.pagos ALTER COLUMN "transacción N°" SET DEFAULT nextval('public.pagos_id_seq'::regclass);
 G   ALTER TABLE public.pagos ALTER COLUMN "transacción N°" DROP DEFAULT;
       public          postgres    false    215    216    216            	          0    16639    carrito 
   TABLE DATA           C   COPY public.carrito (nombre, cantidad, precio, numero) FROM stdin;
    public          postgres    false    218   �                 0    16611    pagos 
   TABLE DATA           I   COPY public.pagos ("transacción N°", monto, fecha, metodo) FROM stdin;
    public          postgres    false    216   "                 0    16596 	   productos 
   TABLE DATA           6   COPY public.productos (name, type, price) FROM stdin;
    public          postgres    false    214   �                 0    16629    usuarios 
   TABLE DATA           2   COPY public.usuarios (usuario, clave) FROM stdin;
    public          postgres    false    217   z                  0    0    carrito_numero_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.carrito_numero_seq', 3, true);
          public          postgres    false    219                       0    0    pagos_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.pagos_id_seq', 13, true);
          public          postgres    false    215            v           2606    16617    pagos pagos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.pagos
    ADD CONSTRAINT pagos_pkey PRIMARY KEY ("transacción N°");
 :   ALTER TABLE ONLY public.pagos DROP CONSTRAINT pagos_pkey;
       public            postgres    false    216            	   9   x�sL)K�+)-J�4�44�45�4�r�3�r-N�e&�pr��ps��qqq R5         �   x�uϻm�0�᚜���/>w��e�k�	�Bh/�9���֒��{ C@|�x��0W�J��@�̭���i��ä��}R[	A����E�1:ø��@�*�S�T�T���U#nm�ӊ��s�,>J!����=Ս͍����\,���B>�d���$���W냎����b����}�Y         �  x�U�Mo�0����LP��ca��j��u��7�
�D�[���ƍGv�N�EW8���+p<w�b��P�M�#�CWj�v���)�'�FF�ؚ����[	d��QՋE�((��i���ؼ2y��'^'�@n��V�t~|��h�?sś�P�'��wc�ơa��1�c�`�!M/R��'p� �V�1�8����<a��s�jr 돠%���Ri�9��hE;aW��#�8�	#�B?S�����D���@�)VxF��(��]���ܣY��tmF�uzZ�uEAڋi4p�{נ�G#��C�Jg��i���c?��(�w�Bi}�% ��q����i֪�G>�w��+�D'�s�]�j3��IZ�X�c9�
=>��I��"�            x�sI�L�Kt�t��\���p���� �q#     