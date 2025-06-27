% Parámetros
r = 1;             % Radio del cilindro
nTheta = 50;       % Número de divisiones en el ángulo
nZ = 50;           % Número de divisiones en Z
h = 2;             % Semialtura (de -h a h, por ejemplo)

% Vectores para theta y z
theta = linspace(0, 2*pi, nTheta);
z     = linspace(-h, h, nZ);

% Malla (grid) de valores de theta y z
[Theta, Z] = meshgrid(theta, z);

% Parametrizaciones de x, y
X = r * cos(Theta);
Y = r * sin(Theta);

% Grafica el cilindro
surf(X, Y, Z);
shading interp;        % Suaviza la superficie
axis equal;            % Escalas iguales en todos los ejes
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Cilindro de radio r');
