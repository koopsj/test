@startuml
skinparam handwritten true

package "On-Premise" as OnPremise {
  component "DB2 DPF Catalog Partition/Coordinator Node" as Coordinator {
    component "Logical node 1" as Logical1
    component "Logical node 2" as Logical2
  }
}
@enduml
