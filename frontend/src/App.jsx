import { useState, useEffect } from "react";
import { Container, Row, Col, Button, Form, Card, Table, Toast } from "react-bootstrap";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [toast, setToast] = useState({ show: false, message: "" });

  // Fetch all tasks
  const fetchTasks = () => {
    fetch("http://127.0.0.1:8000/api/tasks/")
      .then(res => res.json())
      .then(data => setTasks(data))
      .catch(err => console.error(err));
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // Show toast
  const showToast = (message) => {
    setToast({ show: true, message });
    setTimeout(() => setToast({ show: false, message: "" }), 3000);
  };

  // Add new task
  const addTask = () => {
    if (!title) return;
    fetch("http://127.0.0.1:8000/api/tasks/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description, completed: false }),
    })
      .then(res => res.json())
      .then(newTask => {
        setTasks([...tasks, newTask]);
        showToast("Task added successfully!");
      })
      .catch(err => console.error(err));

    setTitle("");
    setDescription("");
  };

  // Delete task
  const deleteTask = (id) => {
    fetch(`http://127.0.0.1:8000/api/tasks/${id}/`, { method: "DELETE" })
      .then(() => {
        setTasks(tasks.filter(t => t.id !== id));
        showToast("Task deleted successfully!");
      })
      .catch(err => console.error(err));
  };

  // Toggle Completed
  const toggleCompleted = (task) => {
    fetch(`http://127.0.0.1:8000/api/tasks/${task.id}/`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: !task.completed }),
    })
      .then(res => res.json())
      .then(updated => {
        setTasks(tasks.map(t => t.id === updated.id ? updated : t));
        showToast("Task status updated!");
      })
      .catch(err => console.error(err));
  };

  return (
    <Container style={{ minHeight: "100vh" }} className="d-flex align-items-center justify-content-center">
      <Row className="w-100 justify-content-center">
        <Col md={10}>
          <Card className="shadow-lg">
            <Card.Body>
              <Card.Title className="text-center mb-4 display-6">Task Manager</Card.Title>

              {/* Add Task Form */}
              <Form
                onSubmit={e => {
                  e.preventDefault();
                  addTask();
                }}
              >
                <Row className="mb-3">
                  <Col md={4}>
                    <Form.Control
                      type="text"
                      placeholder="Enter title..."
                      value={title}
                      onChange={e => setTitle(e.target.value)}
                      required
                    />
                  </Col>
                  <Col md={5}>
                    <Form.Control
                      type="text"
                      placeholder="Enter description..."
                      value={description}
                      onChange={e => setDescription(e.target.value)}
                    />
                  </Col>
                  <Col md={3}>
                    <Button variant="primary" type="submit" className="w-100">
                      Add Task
                    </Button>
                  </Col>
                </Row>
              </Form>

              {/* Tasks Table */}
              <Table striped bordered hover responsive className="text-center mt-3">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Completed</th>
                    <th>Created At</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {tasks.length === 0 ? (
                    <tr>
                      <td colSpan="6">No tasks found</td>
                    </tr>
                  ) : (
                    tasks.map((task, index) => (
                      <tr key={task.id}>
                        <td>{index + 1}</td>
                        <td style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>{task.title}</td>
                        <td style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>{task.description}</td>
                        <td>
                          <Form.Check
                            type="checkbox"
                            checked={task.completed}
                            onChange={() => toggleCompleted(task)}
                          />
                        </td>
                        <td>{new Date(task.created_at).toLocaleString()}</td>
                        <td>
                          <Button variant="danger" size="sm" onClick={() => deleteTask(task.id)}>Delete</Button>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* Toast Notification */}
      <div style={{ position: "fixed", top: 20, right: 20 }}>
        <Toast show={toast.show} bg="success">
          <Toast.Body className="text-white">{toast.message}</Toast.Body>
        </Toast>
      </div>
    </Container>
  );
}

export default App;
