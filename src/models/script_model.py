from sqlalchemy import Column, String, Text, JSON, Integer, Enum, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class ScriptStatus(Enum):
    Active = 'Active'
    Draft = 'Draft'
    Deprecated = 'Deprecated'

class Script(Base):
    __tablename__ = 'scripts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    language = Column(Enum('JavaScript', 'Python', 'Bash', 'Go', 'Ruby', 'PHP', 'Java', 'C', 'C++', 'TypeScript', 'SQL', 'YAML', 'JSON', 'XML', 'HTML', 'CSS', 'Rust', 'Kotlin', 'Swift', name='language_enum'))
    code = Column(Text)
    namespace = Column(String)
    author = Column(String)
    version = Column(String)
    tags = Column(JSON)
    status = Column(Enum(ScriptStatus), default=ScriptStatus.Active)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    execution_count = Column(Integer, default=0)
    last_executed = Column(DateTime)
    endpoint_url = Column(String, unique=True)
    metadata = Column(JSON)

    # Relationships
defines one-to-many relationship for version history and execution logs here
    version_history = ...  # Define your version history relationship
    execution_logs = ...  # Define your execution logs relationship
