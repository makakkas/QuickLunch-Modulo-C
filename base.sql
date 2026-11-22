--Base de datos hecha por GPT

USE cocina_bd;

-- ==========================================
-- 1. CREACIÓN DE PRODUCTOS FICTICIOS
-- ==========================================

INSERT INTO Cocinaapp_producto (nombre, precio, activo)
VALUES
('Pollo con arroz', 4500.00, 1),
('Carne con puré', 4800.00, 1),
('Ensalada César', 3500.00, 1),
('Tallarines boloñesa', 4200.00, 1),
('Lentejas', 3200.00, 1);


-- ==========================================
-- 2. CREACIÓN DE PEDIDOS FICTICIOS
-- ==========================================

INSERT INTO Cocinaapp_pedido
(usuario_id, fecha_servicio, fecha_hora_creacion, estado, estado_preparacion)

SELECT
    u.id,
    '2026-11-22',
    NOW(),
    'confirmado',
    'pendiente'
FROM auth_user u
WHERE u.username = 'trabajador1';


INSERT INTO Cocinaapp_pedido
(usuario_id, fecha_servicio, fecha_hora_creacion, estado, estado_preparacion)

SELECT
    u.id,
    '2026-11-22',
    NOW(),
    'confirmado',
    'en_preparacion'
FROM auth_user u
WHERE u.username = 'trabajador2';


INSERT INTO Cocinaapp_pedido
(usuario_id, fecha_servicio, fecha_hora_creacion, estado, estado_preparacion)

SELECT
    u.id,
    '2026-11-22',
    NOW(),
    'confirmado',
    'preparado'
FROM auth_user u
WHERE u.username = 'trabajador3';


INSERT INTO Cocinaapp_pedido
(usuario_id, fecha_servicio, fecha_hora_creacion, estado, estado_preparacion)

SELECT
    u.id,
    '2026-11-22',
    NOW(),
    'confirmado',
    'pendiente'
FROM auth_user u
WHERE u.username = 'trabajador2';


INSERT INTO Cocinaapp_pedido
(usuario_id, fecha_servicio, fecha_hora_creacion, estado, estado_preparacion)

SELECT
    u.id,
    '2026-11-22',
    NOW(),
    'cancelado',
    'pendiente'
FROM auth_user u
WHERE u.username = 'trabajador1';


INSERT INTO Cocinaapp_pedido
(usuario_id, fecha_servicio, fecha_hora_creacion, estado, estado_preparacion)

SELECT
    u.id,
    '2026-11-23',
    NOW(),
    'confirmado',
    'pendiente'
FROM auth_user u
WHERE u.username = 'trabajador3';


-- ==========================================
-- 3. DETALLES DE LOS PEDIDOS
-- ==========================================

-- Pedido trabajador1: Pollo con arroz (2) y ensalada (1)

INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 2
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Pollo con arroz'
WHERE u.username = 'trabajador1'
AND p.fecha_servicio = '2026-11-22'
AND p.estado = 'confirmado'
AND p.estado_preparacion = 'pendiente';


INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 1
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Ensalada César'
WHERE u.username = 'trabajador1'
AND p.fecha_servicio = '2026-11-22'
AND p.estado = 'confirmado'
AND p.estado_preparacion = 'pendiente';


-- Pedido trabajador2: Carne con puré (1) y lentejas (2)

INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 1
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Carne con puré'
WHERE u.username = 'trabajador2'
AND p.fecha_servicio = '2026-11-22'
AND p.estado = 'confirmado'
AND p.estado_preparacion = 'en_preparacion';


INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 2
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Lentejas'
WHERE u.username = 'trabajador2'
AND p.fecha_servicio = '2026-11-22'
AND p.estado = 'confirmado'
AND p.estado_preparacion = 'en_preparacion';


-- Pedido trabajador3: Tallarines (1) y pollo con arroz (1)

INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 1
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Tallarines boloñesa'
WHERE u.username = 'trabajador3'
AND p.fecha_servicio = '2026-11-22'
AND p.estado = 'confirmado'
AND p.estado_preparacion = 'preparado';


INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 1
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Pollo con arroz'
WHERE u.username = 'trabajador3'
AND p.fecha_servicio = '2026-11-22'
AND p.estado = 'confirmado'
AND p.estado_preparacion = 'preparado';


-- Segundo pedido trabajador2: Tallarines (2)

INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 2
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Tallarines boloñesa'
WHERE u.username = 'trabajador2'
AND p.fecha_servicio = '2026-11-22'
AND p.estado = 'confirmado'
AND p.estado_preparacion = 'pendiente';


-- Pedido cancelado: Pollo con arroz (5)
-- Este pedido debe quedar excluido del consolidado.

INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 5
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Pollo con arroz'
WHERE u.username = 'trabajador1'
AND p.fecha_servicio = '2026-11-22'
AND p.estado = 'cancelado';


-- Pedido del día siguiente: Lentejas (3)

INSERT INTO Cocinaapp_detallepedido (pedido_id, producto_id, cantidad)

SELECT p.id, pr.id, 3
FROM Cocinaapp_pedido p
JOIN auth_user u ON u.id = p.usuario_id
JOIN Cocinaapp_producto pr ON pr.nombre = 'Lentejas'
WHERE u.username = 'trabajador3'
AND p.fecha_servicio = '2026-11-23'
AND p.estado = 'confirmado'
AND p.estado_preparacion = 'pendiente';