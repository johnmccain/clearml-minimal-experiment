from clearml import Task, Logger
task = Task.init(project_name='Test', task_name='Minimal test experiment')
Logger.current_logger().report_text('Successful test', print_console=True)