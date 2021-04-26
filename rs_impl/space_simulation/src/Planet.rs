pub struct Color (i8, i8, i8);

pub struct Planet {
    pub v: [f32; 2],
    pub pos: [f32; 2],
    pub name: String,
    pub color: Color,
    pub radius: i16,
    pub surface_grav: f32,
}

impl Planet {
    pub fn get_radius(&self) -> i16 {
        return self.radius;
    }

    pub fn get_pos(&self) -> (f32, f32) {
        (self.pos[0], self.pos[1])
    }

    pub fn set_pos(&mut self, x: f32, y: f32) {
        self.pos = [x, y];
    }

    pub fn get_color(&self) -> Color {
        self.color
    }

    pub fn set_color(&mut self, color: Color) {
        self.color = color;
    }

    pub fn get_mass(&self) {

    }
}
